# search_face.py
# 人臉追蹤系統 - 透過網路攝影機偵測人臉並控制伺服馬達追蹤
# 提供 MJPEG 串流服務，可透過瀏覽器觀看即時影像

#!/usr/local/bin/python

# 匯入所需的庫
import cv2              # OpenCV 電腦視覺庫
import numpy as np      # 數值計算庫
from http.server import CGIHTTPRequestHandler, HTTPServer  # HTTP 伺服器

# 匯入自訂模組
from myCam1 import myCam    # 攝影機控制模組
from myPWM import mm_close, r_h  # PWM 伺服馬達控制模組

# 全域變數定義
ADJ_DIFF = 80        # 人臉中心與畫面中心的調整閾值（像素）
ADJ_STEP = 1         # 每次調整的角度步長（度）
FRAMEANGLE = 25      # 未使用（可擴充功能用）
SKIPFLAME = 1        # 伺服馬達移動後跳過的影格數

nowAngle = -1        # 當前伺服馬達角度
frame_x_center = 0   # 畫面中心 X 座標
face_x_center = 0    # 人臉中心 X 座標
my_cam = None        # 攝影機物件

# 載入深度學習人臉偵測模型（使用 Caffe 框架）
# deploy.prototxt.txt: 模型架構定義檔
# res10_300x300_ssd_iter_140000.caffemodel: 訓練好的模型權重
net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
CONFIDENCE = 0.6     # 人臉偵測信心度閾值

# 搜尋模式參數（未偵測到人臉時使用）
search_direction = 1  # 搜尋方向：1=向右，-1=向左
SEARCH_STEP = 2       # 搜尋時的角度步長
MOVESKIPFLAME = 10    # 搜尋移動後跳過的影格數


class CamHandler(CGIHTTPRequestHandler):
    """處理 HTTP 請求的處理器，主要提供 MJPEG 串流服務"""
    
    def do_GET(self):
        """處理 HTTP GET 請求"""
        global frame_x_center, face_x_center, search_direction, nowAngle
        
        print(self.path)  # 顯示請求路徑
        
        # 如果是請求 MJPEG 串流
        if self.path.endswith('.mjpg'):
            # 設定 HTTP 回應標頭
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
            
            # 初始化計數器
            count = 0      # 伺服馬達調整後的跳過計數器
            mvCnt = 0      # 搜尋移動後的跳過計數器
            
            try:
                # 主循環：持續讀取影像並處理
                while True:
                    # 從攝影機讀取一幀影像
                    frame = my_cam.read()
                    
                    # 如果還在跳過計數期間，只串流影像不處理
                    if count > 0:
                        count -= 1
                    else:
                        # 獲取影像尺寸
                        (h, w) = frame.shape[:2]
                        frame_x_center = w // 2  # 計算畫面中心
                        
                        # 將影像轉換為深度學習模型所需的格式
                        # 1. 調整大小為 300x300
                        # 2. 減去預訓練模型的平均像素值（BGR順序）
                        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                                    (300, 300), (104.0, 177.0, 123.0))
                        
                        # 將影像輸入模型進行人臉偵測
                        net.setInput(blob)
                        detections = net.forward()
                        
                        # 初始化變數
                        diff = 0          # 人臉與畫面中心的差異
                        new_angle = nowAngle  # 新角度（預設為當前角度）
                        noface = 1        # 是否偵測到人臉的標誌（1=未偵測到）
                        
                        # 如果偵測到任何物件
                        if len(detections) > 0:
                            # 找出信心度最高的人臉（假設只有一張主要人臉）
                            i = np.argmax(detections[0, 0, :, 2])  # 取得最高信心度的索引
                            confidence = detections[0, 0, i, 2]    # 取得最高信心度值
                            
                            # 如果信心度超過閾值，認為是人臉
                            if confidence > CONFIDENCE:
                                noface = 0  # 標記為偵測到人臉
                                
                                # 將正規化座標轉換為實際像素座標
                                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                                (startX, startY, endX, endY) = box.astype("int")
                                
                                # 計算人臉中心 X 座標
                                face_x_center = (startX + endX) // 2
                                print("face_x_center:", face_x_center)
                                
                                # 在影像上標記人臉區域和信心度
                                text = "{:.2f}%".format(confidence * 100)
                                roi = frame[startY:endY, startX:endX]  # 人臉區域
                                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)  # 紅色框
                                y = startY - 10 if startY - 10 > 10 else startY + 10
                                cv2.putText(frame, text, (startX, y),
                                           cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)  # 綠色文字
                                
                                # 計算人臉位置與畫面中心的差異，決定是否需要調整
                                if face_x_center > frame_x_center + ADJ_DIFF:
                                    # 人臉偏右，需要向左轉
                                    diff = face_x_center - frame_x_center
                                    turnR = -1  # 轉動方向（負值為向左）
                                elif frame_x_center > face_x_center + ADJ_DIFF:
                                    # 人臉偏左，需要向右轉
                                    diff = frame_x_center - face_x_center
                                    turnR = 1   # 轉動方向（正值為向右）
                                
                                # 如果有足夠差異需要調整
                                if diff > 0:
                                    # 計算新角度
                                    new_angle = nowAngle + turnR * ADJ_STEP
                                    
                                    # 確保角度在有效範圍內（0-180度）
                                    if new_angle < 0:
                                        new_angle = 0
                                    elif new_angle > 180:
                                        new_angle = 180
                                
                                # 如果角度有變化，控制伺服馬達轉動
                                if new_angle != nowAngle:
                                    nowAngle = r_h(new_angle, 0.16, nowAngle, frame_x_center, face_x_center)
                                    count = SKIPFLAME      # 設定跳過計數
                                    mvCnt = MOVESKIPFLAME  # 重置搜尋跳過計數
                        
                        # 如果未偵測到人臉，進入搜尋模式
                        if noface:
                            if mvCnt > 0:
                                # 仍在搜尋移動後的冷卻期
                                mvCnt -= 1
                            else:
                                # 計算搜尋的下一個角度
                                new_angle = nowAngle + SEARCH_STEP * search_direction
                                
                                # 檢查邊界，反轉搜尋方向
                                if new_angle > 180:
                                    new_angle = 180 - SEARCH_STEP
                                    search_direction = -1  # 轉為向左搜尋
                                elif new_angle < 0:
                                    new_angle = SEARCH_STEP
                                    search_direction = 1   # 轉為向右搜尋
                                
                                # 控制伺服馬達轉動到搜尋角度
                                nowAngle = r_h(new_angle, 0.1, nowAngle)
                    
                    # 將影像編碼為 JPEG 格式
                    r, buf = cv2.imencode(".jpg", frame)
                    
                    # 發送 MJPEG 串流數據
                    self.wfile.write(b"--jpgboundary\r\n")
                    self.send_header('Content-type', 'image/jpeg')
                    self.send_header('Content-length', str(len(buf)))
                    self.end_headers()
                    self.wfile.write(bytearray(buf))
                    self.wfile.write(b'\r\n')
                    
            except KeyboardInterrupt:
                # 處理鍵盤中斷（Ctrl+C）
                print(' End server : 鍵盤 Ctrl-C 中斷')
                raise SystemExit('鍵盤中斷')
            except Exception as e:
                # 處理一般異常
                print(f'End server : Exception, {e}')
                raise SystemExit
            except SystemExit as e:
                # 處理系統退出
                print(f'End server : SystemExit, {e}')
                raise
            except:
                # 處理其他未知錯誤
                print('End server : Some Error')
                raise SystemExit
            finally:
                # 伺服器結束時的清理工作
                print('網站伺服器結束⌛')


def main():
    """主函數：初始化系統並啟動伺服器"""
    global my_cam, nowAngle
    
    # 初始化攝影機
    my_cam = myCam()
    
    try:
        # 初始化伺服馬達到預設角度
        nowAngle = r_h()
        
        # 建立並啟動 HTTP 伺服器
        # 參數1: 伺服器地址（空字串表示本機所有介面）
        # 參數2: 連接埠號
        # 參數3: 請求處理器類別
        server = HTTPServer(('', 9090), CamHandler)
        print("server started 請用瀏覽器看我👀")
        
        # 開始服務（持續運行直到中斷）
        server.serve_forever()
        
    except KeyboardInterrupt:
        # 處理鍵盤中斷
        print(' End program : 鍵盤 Ctrl-C 中斷')
    except Exception as e:
        # 處理一般異常
        print(f'End program : Exception, {e}')
    except SystemExit as e:
        # 處理系統退出
        print(f'End program : SystemExit, {e}')
    except:
        # 處理其他未知錯誤
        print('End program : Some Error')
    finally:
        # 程式結束時的清理工作
        my_cam.release()      # 釋放攝影機資源
        server.socket.close()  # 關閉伺服器 Socket
        mm_close()            # 執行 PWM 模組的清理函數
        print('程式結束')


# 程式進入點
if __name__ == '__main__':
    main()
