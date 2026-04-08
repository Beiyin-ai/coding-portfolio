import cv2
import base64
import threading
import time
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
from fastmcp import FastMCP

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--video', default='/dev/video0', help='video')
args = parser.parse_args()

# ==========================================
# 1. 攝影機背景讀取管理
# ==========================================
class CameraManager:
    def __init__(self, src):
        self.src = src
        self.cap = cv2.VideoCapture(self.src)
        self.latest_jpeg_bytes = None
        self.lock = threading.Lock()
        self.running = True
        self.thread = threading.Thread(target=self._update_frames, daemon=True)
        self.thread.start()

    def _update_frames(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                success, buffer = cv2.imencode(".jpg", frame)
                if success:
                    with self.lock:
                        self.latest_jpeg_bytes = buffer.tobytes()
            time.sleep(0.03)

    def get_latest_jpeg(self):
        with self.lock:
            return self.latest_jpeg_bytes

    def release(self):
        self.running = False
        self.cap.release()

camera = CameraManager(args.video)

# ==========================================
# 2. FastAPI Debug 伺服器 (Port 8818)
# ==========================================
app = FastAPI()

def mjpeg_generator():
    while True:
        jpeg_bytes = camera.get_latest_jpeg()
        if jpeg_bytes:
            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + jpeg_bytes + b"\r\n")
        time.sleep(0.05)

@app.get("/mymcp_cam.mjpg")
def video_feed():
    return StreamingResponse(mjpeg_generator(), media_type="multipart/x-mixed-replace; boundary=frame")

def start_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8818, log_level="warning")

# ==========================================
# 3. FastMCP 伺服器 (Port 8808)
# ==========================================
mcp = FastMCP("RPi_Camera_Server")

@mcp.tool()
def get_frame() -> str:
    """獲取 USB 攝影機的最新畫面。回傳：Base64 編碼的 JPEG 圖片 (Data URI 格式字串)"""
    jpeg_bytes = camera.get_latest_jpeg()
    if not jpeg_bytes:
        return "Error: 目前無法從攝影機取得畫面，請檢查硬體連線。"
    base64_str = base64.b64encode(jpeg_bytes).decode("utf-8")
    return f"data:image/jpeg;base64,{base64_str}"

# ==========================================
# 4. 主程式執行區
# ==========================================
if __name__ == "__main__":
    print("啟動 FastAPI Debug 伺服器於 http://localhost:8818/mymcp_cam.mjpg ...")
    api_thread = threading.Thread(target=start_fastapi, daemon=True)
    api_thread.start()

    print("啟動 FastMCP 伺服器 (SSE) 於 port 8808 ...")
    try:
        mcp.run(transport="sse", host="0.0.0.0", port=8808)
    finally:
        camera.release()
