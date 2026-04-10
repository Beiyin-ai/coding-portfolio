import asyncio
import json
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from contextlib import AsyncExitStack
from openai import AsyncOpenAI
from fastmcp import Client

# ==========================================
# 1. 系統設定參數
# ==========================================
LLM_BASE_URL = "http://localhost:8880/v1"
MODEL_NAME = "qwen3-vl-2b-instruct"

# MCP 伺服器端點設定
CAMERA_MCP_URL = "http://127.0.0.1:8808/sse"      # 請替換為 RPi 的實際 IP
PTZ_MCP_URL = "http://192.168.8.181:80/mcp"      # 你的 ESP32 SG90 伺服器 (維持原樣)
MONITOR_SCRIPT_PATH = "mcp_msg.g1.py"

latest_image_data_uri = ""

# ==========================================
# 2. 建立 Agent 內建的影像顯示伺服器 (Port 8828)
# ==========================================
app_img = FastAPI()

@app_img.get("/")
async def view_image():
    html = """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Agent 視覺監控畫面</title>
        <style>
            body { background-color: #121212; color: white; text-align: center; font-family: sans-serif; }
            img { max-width: 80%; border: 3px solid #4CAF50; border-radius: 8px; margin-top: 20px; }
            .status { margin-top: 10px; color: #aaa; }
        </style>
    </head>
    <body>
        <h2>Agent 當前看到的畫面 (Port 8828)</h2>
        <img id="cam" src="" alt="等待影像傳入..." />
        <div class="status" id="status_text">連線中...</div>
        <script>
            setInterval(() => {
                fetch('/image')
                    .then(r => r.text())
                    .then(data => {
                        if(data && data.startsWith('data:image')) {
                            document.getElementById('cam').src = data;
                            document.getElementById('status_text').innerText = "畫面更新中 (" + new Date().toLocaleTimeString() + ")";
                        }
                    })
                    .catch(err => console.error(err));
            }, 500);
        </script>
    </body>
    </html>
    """
    return HTMLResponse(html)

@app_img.get("/image")
async def get_image():
    return PlainTextResponse(latest_image_data_uri)

async def run_image_server():
    config = uvicorn.Config(app_img, host="0.0.0.0", port=8828, log_level="error")
    server = uvicorn.Server(config)
    await server.serve()

# ==========================================
# 3. Agent 主體邏輯
# ==========================================
async def main():
    global latest_image_data_uri
    
    print("啟動 Agent 內部影像伺服器於 http://localhost:8828 ...")
    asyncio.create_task(run_image_server())

    llm_client = AsyncOpenAI(api_key="sk-no-key-required", base_url=LLM_BASE_URL)
    last_log_message = ""

    async with AsyncExitStack() as stack:
        print("正在連接各個 MCP 伺服器...")
        
        try:
            monitor_client = await stack.enter_async_context(Client(MONITOR_SCRIPT_PATH))
            print("✅ Monitor MCP (stdio) 連線成功！(可於 Port 8817 觀看文字日誌)")

            camera_client = await stack.enter_async_context(Client(CAMERA_MCP_URL))
            print("✅ Camera MCP (SSE) 連線成功！")

            ptz_client = await stack.enter_async_context(Client(PTZ_MCP_URL))
            print("✅ PTZ Control MCP 連線成功！")

        except Exception as e:
            print(f"❌ 伺服器連線失敗: {e}")
            return

        async def log_to_web(msg: str):
            nonlocal last_log_message
            if msg != last_log_message:
                try:
                    await monitor_client.call_tool("send_log_to_web", {"message": msg})
                    print(f"[Log] {msg}")
                    last_log_message = msg
                except Exception as e:
                    print(f"日誌發送失敗: {e}")

        await log_to_web("系統初始化完成，開始執行視覺監控任務...")
        
        # 伺服馬達控制狀態
        current_angle = 90       # 初始設定在正中間
        sweep_direction = 1      # 1 代表角度增加，-1 代表角度減少
        STEP_SIZE = 15           # 每次微調/搜尋轉動的度數

        # 先將鏡頭歸位到中間
        await ptz_client.call_tool("set_servo_angle", {"angle": current_angle})

        # ==========================================
        # 4. 核心監控迴圈
        # ==========================================
        try:
            while True:
                # 步驟 A: 獲取攝影機畫面
                try:
                    cam_raw_result = await camera_client.call_tool("get_frame", {})
                    base64_image_url = cam_raw_result.content[0].text
                    
                    if "Error" in base64_image_url:
                        await log_to_web(f"⚠️ 鏡頭讀取異常: {base64_image_url}")
                        await asyncio.sleep(2)
                        continue
                    
                    latest_image_data_uri = base64_image_url

                except Exception as e:
                    await log_to_web(f"⚠️ 無法取得攝影機畫面，可能連線中斷: {e}")
                    await asyncio.sleep(2)
                    continue

                # 步驟 B: 組裝 prompt 讓 Qwen-VL 分析
                prompt_text = """
                請分析這張圖片，並以嚴格的 JSON 格式回覆，不要包含任何其他文字或 Markdown 標記。
                需要判斷以下幾點：
                1. 畫面是否全黑或鏡頭明顯被遮擋？
                2. 畫面中是否有「人」、「貓」、「狗」或「動物的填充玩偶」？
                3. 如果有找到目標物，它大致位於畫面的哪裡？(left, center, right)

                請輸出如下 JSON 格式：
                {
                    "is_blocked_or_black": true/false,
                    "target_found": true/false,
                    "target_position": "left" / "center" / "right" / "none",
                    "reason": "簡短說明你看到了什麼"
                }
                """

                # 步驟 C: 呼叫本地 LLM 推論
                try:
                    response = await llm_client.chat.completions.create(
                        model=MODEL_NAME,
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": prompt_text},
                                    {"type": "image_url", "image_url": {"url": latest_image_data_uri}}
                                ]
                            }
                        ],
                        temperature=0.1,
                        response_format={"type": "json_object"}
                    )
                    
                    vision_result = response.choices[0].message.content
                    data = json.loads(vision_result)
                    
                    is_blocked = data.get("is_blocked_or_black", False)
                    target_found = data.get("target_found", False)
                    target_pos = data.get("target_position", "none")
                    reason = data.get("reason", "")

                except Exception as e:
                    await log_to_web(f"⚠️ 視覺分析發生錯誤: {e}")
                    await asyncio.sleep(2)
                    continue

                # 步驟 D: 根據 AI 判斷執行對應動作
                if is_blocked:
                    await log_to_web(f"🚨 警告：鏡頭畫面全黑或被遮住了！({reason})")
                    await asyncio.sleep(2)
                    continue

                if target_found:
                    if target_pos == "center":
                        await log_to_web(f"🎯 找到目標物並鎖定在畫面中央！目前角度: {current_angle}° ({reason})")
                    
                    elif target_pos == "left":
                        await log_to_web(f"👀 在左側發現目標物，攝影機向左微調中... ({reason})")
                        current_angle = min(180, current_angle + STEP_SIZE)
                        await ptz_client.call_tool("set_servo_angle", {"angle": current_angle})
                    
                    elif target_pos == "right":
                        await log_to_web(f"👀 在右側發現目標物，攝影機向右微調中... ({reason})")
                        current_angle = max(0, current_angle - STEP_SIZE)
                        await ptz_client.call_tool("set_servo_angle", {"angle": current_angle})
                else:
                    await log_to_web(f"🔍 畫面中沒有目標物，鏡頭搜尋中 (角度: {current_angle}°)")
                    
                    current_angle += (STEP_SIZE * sweep_direction)

                    if current_angle >= 180:
                        current_angle = 180
                        sweep_direction = -1
                        await log_to_web("🔄 鏡頭到底了 (180°)，準備反向搜尋")
                    elif current_angle <= 0:
                        current_angle = 0
                        sweep_direction = 1
                        await log_to_web("🔄 鏡頭到底了 (0°)，準備反向搜尋")

                    try:
                        await ptz_client.call_tool("set_servo_angle", {"angle": current_angle})
                    except Exception as e:
                        await log_to_web(f"⚠️ 鏡頭轉動控制失敗: {e}")

                await asyncio.sleep(0.5)

        except KeyboardInterrupt:
            print("\n接收到 Ctrl-C 中斷訊號，正在關閉系統...")
            await log_to_web("🛑 系統接收到中斷訊號，正在安全關閉連線...")
        finally:
            print("所有連線已安全關閉，Agent 結束運行。")

if __name__ == "__main__":
    asyncio.run(main())