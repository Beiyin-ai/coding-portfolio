#!/usr/bin/env python3
"""
物體偵測與追蹤系統
支援 MobileNetSSD 20 種物體類別
"""

import cv2
import numpy as np
from http.server import CGIHTTPRequestHandler, HTTPServer
import threading
import time
import argparse

# 自訂模組
from myCam1 import myCam
from myPWM import mm_close, r_h

# 常數設定
ADJ_DIFF = 80
ADJ_STEP = 1
FRAMEANGLE = 25
SKIPFLAME = 1
CONFIDENCE = 0.6

# 全域變數
nowAngle = -1
frame_x_center = 0
face_x_center = 0
my_cam = None
search_direction = 1
SEARCH_STEP = 1
MOVESKIPFLAME = 1
serving = True
frm_HTTP = None

# 命令列參數解析
parser = argparse.ArgumentParser(
parser.add_argument(
)
args = parser.parse_args()

# 檢查參數有效性
if args.object > 20 or args.object < 1:
    print("錯誤：物體編號必須在 1-20 之間")
    exit(1)

obiectNum = args.object

# 載入 MobileNetSSD 模型
net = cv2.dnn.readNetFromCaffe(
    "../models/MobileNetSSD_deploy.prototxt",
    "../models/MobileNetSSD_deploy.caffemodel"
)


class CamHandler(CGIHTTPRequestHandler):
    """處理 HTTP 串流請求"""
    
    def do_GET(self):
        print(f"Request path: {self.path}")
        
            self.send_response(200)
            self.end_headers()
            
            while serving:
                if frm_HTTP is None:
                    time.sleep(0.1)
                    continue
                    
                r, buf = cv2.imencode(".jpg", frm_HTTP)
                self.wfile.write(b"--jpgboundary\r\n")
                self.end_headers()
                self.wfile.write(bytearray(buf))
                
    
    def log_message(self, format, *args):
        """覆寫日誌訊息，避免輸出到終端機"""
        pass


def main():
    """主程式"""
    global frame_x_center, face_x_center, search_direction
    global my_cam, frm_HTTP, nowAngle, serving
    
    # 初始化攝影機
    my_cam = myCam()
    
    # 顯示偵測的物體類別
    class_names = {
    
    try:
        nowAngle = r_h()
        
        # 啟動 HTTP 伺服器
        threading.Thread(
            target=server.serve_forever,
            daemon=True,
            args=()
        ).start()
        print("server started 請用瀏覽器看我👀")
        print("網址: http://<樹莓派IP>:9090/a.mjpg")
        
        # 初始化影片寫入器
        vwriter = cv2.VideoWriter()
        fps = 30
        vwriter.open(
            fps,
            my_cam.getProp_W_H(),
            True
        )
        
        count = 0
        mvCnt = 0
        
        while True:
            frame = my_cam.read()
            if count > 0:
                count -= 1
            else:
                (h, w) = frame.shape[:2]
                frame_x_center = w // 2
                
                # 物體偵測
                blob = cv2.dnn.blobFromImage(
                    cv2.resize(frame, (300, 300)),
                    0.007843,
                    (300, 300),
                    (127.5, 127.5, 127.5)
                )
                net.setInput(blob)
                detections = net.forward()
                
                diff = 0
                new_angle = nowAngle
                noface = 1
                
                if len(detections) > 0:
                    # 尋找指定類別的偵測結果
                    ixay = np.argwhere(detections[0, 0, :, 1] == obiectNum).flatten()
    
    def do_GET(self):
        print(f"Request path: {self.path}")
        
            self.send_response(200)
            self.end_headers()
            
            while serving:
                if frm_HTTP is None:
                    time.sleep(0.1)
                    continue
                    
                r, buf = cv2.imencode(".jpg", frm_HTTP)
                self.wfile.write(b"--jpgboundary\r\n")
                self.end_headers()
                self.wfile.write(bytearray(buf))
                
    
    def do_GET(self):
        print(f"Request path: {self.path}")
        
            self.send_response(200)
            self.end_headers()
            
            while serving:
                if frm_HTTP is None:
                    time.sleep(0.1)
                    continue
                    
                r, buf = cv2.imencode(".jpg", frm_HTTP)
                self.wfile.write(b"--jpgboundary\r\n")
                self.end_headers()
                self.wfile.write(bytearray(buf))
                
