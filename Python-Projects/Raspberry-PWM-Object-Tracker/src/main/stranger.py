#!/usr/bin/env python3
"""
陌生人偵測與臉部辨識系統
使用樹莓派 + OpenCV + 臉部辨識
"""

import cv2
import numpy as np
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time
import face_recognition

# 自訂模組
from myCam1 import myCam
from myPWM import mm_close, r_h

# 常數設定
ADJ_DIFF = 80
ADJ_STEP = 1
FRAMEANGLE = 25
SKIPFLAME = 1
CONFIDENCE = 0.6
OBJ_NUM = 15  # person class in MobileNetSSD
SEARCH_STEP = 2
MOVESKIPFLAME = 1

# 全域變數
nowAngle = -1
frame_x_center = 0
face_x_center = 0
my_cam = None
search_direction = 1
serving = True
frm_HTTP = None

# 載入 MobileNetSSD 模型
net = cv2.dnn.readNetFromCaffe(
    "../models/MobileNetSSD_deploy.prototxt",
    "../models/MobileNetSSD_deploy.caffemodel"
)


class CamHandler(BaseHTTPRequestHandler):
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
    
    # 載入已知臉部編碼
    try:
        Co_P_encoding = face_recognition.face_encodings(
            face_recognition.load_image_file("../img/Co-p.jpg")
        )[0]
        chinese_encoding = face_recognition.face_encodings(
            face_recognition.load_image_file("../img/chinese.jpg")
        )[0]
        english_encoding = face_recognition.face_encodings(
            face_recognition.load_image_file("../img/english.jpg")
        )[0]
        
        known_face_encodings = [
            Co_P_encoding,
            chinese_encoding,
            english_encoding
        ]
        known_face_names = [
            "Co-P",
            "chinese",
            "english"
        ]
    except Exception as e:
        print(f"載入臉部圖片錯誤: {e}")
        known_face_encodings = []
        known_face_names = []
    
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    
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
                    # 尋找 person 類別的偵測結果
                    ixay = np.argwhere(detections[0, 0, :, 1] == OBJ_NUM).flatten()
                    if len(ixay) > 0:
                        # 取信賴度最高的偵測結果
                        iix = np.argmax(np.take(detections[0, 0, :, 2], ixay))
                        i = ixay[iix]
                        confidence = detections[0, 0, i, 2]
                        
                        if confidence > CONFIDENCE:
                            noface = 0
                            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                            (startX, startY, endX, endY) = box.astype("int")
                            face_x_center = (startX + endX) // 2
                            print("object_x_center:", face_x_center)

                            # 臉部辨識
                            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            face_locations = face_recognition.face_locations(rgb_frame)
                            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                            face_names = []
                            hasUnknown = len(face_locations)
                            
                            for face_encoding in face_encodings:
                                matches = face_recognition.compare_faces(
                                    known_face_encodings,
                                    face_encoding
                                )
                                name = "Unknown"
                                face_distances = face_recognition.face_distance(
                                    known_face_encodings,
                                    face_encoding
                                )
                                best_match_index = np.argmin(face_distances)
                                
                                if face_distances[best_match_index] < 0.6 and matches[best_match_index]:
                                    name = known_face_names[best_match_index]
                                    hasUnknown -= 1
                                face_names.append(name)

                            # 繪製臉部框和標籤
                            if len(face_locations):
                                for (top, right, bottom, left), name in zip(face_locations, face_names):
                                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                                    font = cv2.FONT_HERSHEY_DUPLEX
                                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                            else:
                                hasUnknown = 1
                                text = "{:.2f}%".format(confidence * 100)
                                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
                                y = startY - 10 if startY - 10 > 10 else startY + 10
                                cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
                            
                            # 錄製陌生人影片
                            if hasUnknown:
                                vwriter.write(frame)
                            
                            # 計算角度調整
                            if face_x_center > frame_x_center + ADJ_DIFF:
                                diff = face_x_center - frame_x_center
                                turnR = -1
                            elif frame_x_center > face_x_center + ADJ_DIFF:
                                diff = frame_x_center - face_x_center
                                turnR = 1
                            
                            if diff > 0:
                                new_angle = nowAngle + turnR * ADJ_STEP
                                if new_angle < 0:
                                    new_angle = 0
                                elif new_angle > 180:
                                    new_angle = 180
                            
                            if new_angle != nowAngle:
                                nowAngle = r_h(new_angle, 0.16, nowAngle, frame_x_center, face_x_center)
                                count = SKIPFLAME
                                mvCnt = MOVESKIPFLAME
                
                # 搜尋模式
                if noface:
                    if mvCnt > 0:
                        mvCnt -= 1
                    else:
                        new_angle = nowAngle + SEARCH_STEP * search_direction
                        if new_angle > 180:
                            new_angle = 180 - SEARCH_STEP
                            search_direction = -1
                        elif new_angle < 0:
                            new_angle = SEARCH_STEP
                            search_direction = 1
                        nowAngle = r_h(new_angle, 0.1, nowAngle)
            
            frm_HTTP = frame.copy()
    
    except KeyboardInterrupt:
    except Exception as e:
    except SystemExit as e:
    except:
    finally:
        serving = False
        vwriter.release()
        my_cam.release()
        server.socket.close()
        mm_close()


