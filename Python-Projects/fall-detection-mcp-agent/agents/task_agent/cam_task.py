import cv2
import argparse
import base64
import threading
import time
import os
import paho.mqtt.client as mqtt
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastmcp import FastMCP

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--video", default="0", help="Camera index, mp4 path, or URL (rtsp/http)")
parser.add_argument("-m", "--message", default=None, help="Startup MQTT message (Retained)")
args = parser.parse_args()

if args.message:
    try:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.connect("172.17.0.1", 1883, 60)
        client.publish("agent/task", args.message, retain=True)
        client.disconnect()
        print(f"📡 已發佈保留任務：{args.message}")
    except Exception as e:
        print(f"❌ MQTT 發佈失敗: {e}")

mcp = FastMCP("CameraServer")
app = FastAPI()
latest_frame = None
frame_lock = threading.Lock()

def camera_loop():
    global latest_frame
    source = args.video
    if source.isdigit():
        source = int(source)
    
    while True:
        cap = cv2.VideoCapture(source)
        while cap.isOpened():
            success, frame = cap.read()
            if success:
                with frame_lock:
                    latest_frame = frame.copy()
                time.sleep(0.03)
            else:
                break
        cap.release()
        if isinstance(source, int) or (isinstance(source, str) and not source.endswith(('.mp4', '.avi'))):
            print("⚠️ 串流中斷，2秒後重連...")
            time.sleep(2)
        else:
            time.sleep(0.1)

threading.Thread(target=camera_loop, daemon=True).start()

@app.get("/mymcp_cam.mjpg")
async def video_feed():
    def gen():
        while True:
            with frame_lock:
                if latest_frame is not None:
                    _, buffer = cv2.imencode('.jpg', latest_frame)
                    yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
            time.sleep(0.04)
    return StreamingResponse(gen(), media_type="multipart/x-mixed-replace; boundary=frame")

@mcp.tool()
async def get_frame() -> str:
    with frame_lock:
        if latest_frame is None:
            return "Error: No frame"
        _, buffer = cv2.imencode('.jpg', latest_frame)
        return base64.b64encode(buffer).decode('utf-8')

if __name__ == "__main__":
    threading.Thread(target=lambda: mcp.run(transport="sse", port=8808), daemon=True).start()
    threading.Thread(target=lambda: uvicorn.run(app, host="0.0.0.0", port=8818, log_level="critical"), daemon=True).start()
    
    try:
        print("🎥 Camera 伺服器已啟動。(按 Ctrl-C 強制關閉)")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 收到 Ctrl-C，Camera 伺服器秒殺關閉！")
        os._exit(0)