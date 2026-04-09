import threading
import time
import asyncio
from datetime import datetime
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
from fastmcp import FastMCP

# ==========================================
# 1. 訊息儲存與全域變數
# ==========================================
global_messages = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Agent 即時訊息監控</title>
    <style>
        body {
            font-family: "Consolas", "Courier New", monospace;
            background-color: #1e1e1e;
            color: #d4d4d4;
            margin: 0;
            padding: 20px;
        }
        h2 { color: #4fc1ff; border-bottom: 1px solid #333; padding-bottom: 10px; }
        #messages-container {
            height: 85vh;
            overflow-y: auto;
            background-color: #252526;
            border: 1px solid #3d3d3d;
            padding: 15px;
            border-radius: 5px;
        }
        .message-line {
            margin-bottom: 8px;
            border-bottom: 1px dashed #333;
            padding-bottom: 4px;
        }
        .timestamp { color: #ce9178; margin-right: 12px; }
        .content { color: #dcdcaa; }
    </style>
</head>
<body>
    <h2>Agent 即時訊息監控終端</h2>
    <div id="messages-container"></div>
    <script>
        const container = document.getElementById("messages-container");
        const ws = new WebSocket("ws://" + location.host + "/ws");
        ws.onmessage = function(event) {
            const div = document.createElement("div");
            div.className = "message-line";
            div.innerHTML = event.data;
            container.appendChild(div);
            container.scrollTop = container.scrollHeight;
        };
        ws.onclose = function() {
            const div = document.createElement("div");
            div.className = "message-line";
            div.innerHTML = "<span class=\\"timestamp\\">[系統]</span> <span class=\\"content\\" style=\\"color: red;\\">連線已斷開，請重新整理頁面。</span>";
            container.appendChild(div);
        };
    </script>
</body>
</html>
"""

# ==========================================
# 2. FastAPI 網頁與 WebSocket 伺服器
# ==========================================
app = FastAPI()

@app.get("/")
async def get_monitor_page():
    return HTMLResponse(content=HTML_TEMPLATE)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    for msg in global_messages:
        await websocket.send_text(msg)
    last_index = len(global_messages)
    try:
        while True:
            current_index = len(global_messages)
            if current_index > last_index:
                for i in range(last_index, current_index):
                    await websocket.send_text(global_messages[i])
                last_index = current_index
            await asyncio.sleep(0.1)
    except Exception:
        pass

def start_web_server():
    uvicorn.run(app, host="0.0.0.0", port=8817, log_level="error", access_log=False)

# ==========================================
# 3. FastMCP 伺服器 (stdio)
# ==========================================
mcp = FastMCP("MonitorServer")

@mcp.tool()
def send_log_to_web(message: str) -> str:
    """將訊息傳送並顯示在 port 8817 的監控網頁上。"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"<span class=\\"timestamp\\">[{timestamp}]</span> <span class=\\"content\\">{message}</span>"
    global_messages.append(formatted_msg)
    return "訊息已成功發送至監控網頁。"

# ==========================================
# 4. 主程式執行區
# ==========================================
if __name__ == "__main__":
    web_thread = threading.Thread(target=start_web_server, daemon=True)
    web_thread.start()
    mcp.run(transport="stdio")
