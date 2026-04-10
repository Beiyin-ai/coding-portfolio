import asyncio
import base64
import cv2
import numpy as np
import paho.mqtt.client as mqtt
import uvicorn
import aiohttp
import os
import threading
import time
from contextlib import asynccontextmanager, AsyncExitStack
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.client.stdio import stdio_client, StdioServerParameters

log_session = None
loop = None
current_frame = None
last_msg = ""
current_task_handler = None
task_counter = 0

@asynccontextmanager
async def lifespan(app: FastAPI):
    global log_session, loop, mqtt_client
    loop = asyncio.get_running_loop()
    server_params = StdioServerParameters(command="uv", args=["run", "mcp_message.py"])
    
    async with AsyncExitStack() as stack:
        try:
            print("🚀 Agent 啟動中...")
            log_read, log_write = await stack.enter_async_context(stdio_client(server_params))
            log_session = await stack.enter_async_context(ClientSession(log_read, log_write))
            await log_session.initialize()
            
            mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            mqtt_client.on_message = on_message
            mqtt_client.connect("172.17.0.1", 1883)
            mqtt_client.subscribe("agent/task")
            mqtt_client.loop_start()
            print("✅ 系統就緒，監控與日誌已啟用。")
            yield
        finally:
            if mqtt_client:
                mqtt_client.loop_stop()

app = FastAPI(lifespan=lifespan)

def on_message(client, userdata, msg):
    global current_task_handler, task_counter
    payload = msg.payload.decode()
    if loop and loop.is_running():
        task_counter += 1
        if current_task_handler and not current_task_handler.done():
            current_task_handler.cancel()
        current_task_handler = asyncio.run_coroutine_threadsafe(
            process_task(payload, task_counter), loop
        )

async def analyze_image(img_b64: str, task_desc: str) -> str:
    url = "http://localhost:8880/v1/chat/completions"
    payload = {
        "model": "Qwen3-VL-2B-Instruct-Q4_K_M",
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": f"簡短回答任務：{task_desc}"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
        ]}],
        "max_tokens": 100, "temperature": 0.1
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=30) as resp:
                if resp.status == 200:
                    res = await resp.json()
                    return res['choices'][0]['message']['content'].strip()
    except Exception:
        return "LLM 分析暫時無法連線"
    return "無回應"

async def fetch_frames_bg(cam_session):
    global current_frame
    while True:
        try:
            result = await cam_session.call_tool("get_frame", arguments={})
            if "Error" not in result.content[0].text:
                current_frame = base64.b64decode(result.content[0].text)
            await asyncio.sleep(0.03)
        except asyncio.CancelledError:
            break
        except Exception:
            await asyncio.sleep(0.5)

async def process_task(task_desc, task_id):
    global current_frame, last_msg, task_counter
    last_msg = ""
    fetch_task = None
    print(f"\n🔥 開始任務：{task_desc}")
    
    try:
        async with sse_client("http://localhost:8808/sse") as (cam_read, cam_write):
            async with ClientSession(cam_read, cam_write) as cam_session:
                await cam_session.initialize()
                fetch_task = asyncio.create_task(fetch_frames_bg(cam_session))
                
                while True:
                    if current_frame:
                        img_b64 = base64.b64encode(current_frame).decode('utf-8')
                        analysis = await analyze_image(img_b64, task_desc)
                        if analysis != last_msg:
                            await log_session.call_tool("send_log_to_web", arguments={"message": analysis})
                            last_msg = analysis
                        
                        if "任務結束" in analysis or "沒有畫面" in analysis:
                            print("🏁 LLM 判斷任務結束。")
                            break
                    await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass
    except Exception:
        print("⚠️ Camera 伺服器連線異常或已中斷。")
    finally:
        if fetch_task:
            fetch_task.cancel()
        if task_counter == task_id:
            current_frame = None

@app.get("/monitor")
async def monitor():
    async def stream():
        while True:
            frame = current_frame
            if frame is None:
                img = np.zeros((480, 640, 3), dtype=np.uint8)
                cv2.putText(img, "WAITING FOR TASK", (150, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                _, buffer = cv2.imencode('.jpg', img)
                frame = buffer.tobytes()
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            await asyncio.sleep(0.04)
    return StreamingResponse(stream(), media_type="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    threading.Thread(target=lambda: uvicorn.run(app, host="0.0.0.0", port=8828, log_level="critical"), daemon=True).start()
    
    try:
        print("🤖 Agent 伺服器已啟動。(按 Ctrl-C 強制關閉)")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 收到 Ctrl-C，Agent 伺服器秒殺關閉！")
        os._exit(0)