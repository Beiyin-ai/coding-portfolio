#!/usr/local/bin/python
# vplay.py - 影片/攝影機串流伺服器
# 功能：將影片檔案或攝影機畫面透過 MJPEG 串流到網頁瀏覽器
# 使用方法：python vplay.py -v output.mp4 -s 20   # 每0.2秒一畫面（0.01秒 x 20）

import cv2              # OpenCV 電腦視覺庫，用於影片處理
from http.server import CGIHTTPRequestHandler, HTTPServer  # HTTP 伺服器
import time            # 時間控制
import argparse        # 命令列參數解析

# 設定命令列參數解析器
parser = argparse.ArgumentParser(description='影片/攝影機串流伺服器')
parser.add_argument('-v', '--video', help='影片檔案路徑（若不指定則使用攝影機）')
parser.add_argument('-s', '--speed', default=0, type=int,
                   help='播放速度：每多少厘秒（centisecond，百分之一秒）一畫面，0表示全速播放')

# 解析命令列參數
args = parser.parse_args()

# 全域變數：影片擷取物件
capture = None

class CamHandler(CGIHTTPRequestHandler):
    """HTTP 請求處理器，負責處理 MJPEG 串流請求"""
    
    def do_GET(self):
        """處理 HTTP GET 請求"""
        global capture
        
        print(f'請求路徑：{self.path}')
        
        # 檢查是否請求 MJPEG 串流
        if self.path.endswith('.mjpg'):
            # 設定 HTTP 回應標頭
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
            
            # 計算畫面間隔時間（將厘秒轉換為秒）
            sleeps = args.speed * 0.01
            
            try:
                # 主循環：持續讀取並發送影像畫面
                while True:
                    # 讀取一幀影像
                    rc, frame = capture.read()
                    
                    # 如果讀取失敗（影片結束或攝影機錯誤）
                    if not rc:
                        # 如果是影片檔案，重新開始播放
                        if args.video:
                            capture = cv2.VideoCapture(args.video)
                        continue
                    
                    # 將影像編碼為 JPEG 格式
                    r, buf = cv2.imencode('.jpg', frame)
                    
                    # 發送 MJPEG 串流數據
                    self.wfile.write(b'--jpgboundary\r\n')
                    self.send_header('Content-type', 'image/jpeg')
                    self.send_header('Content-length', str(len(buf)))
                    self.end_headers()
                    self.wfile.write(bytearray(buf))
                    self.wfile.write(b'\r\n')
                    
                    # 控制播放速度
                    time.sleep(sleeps)
                    
            except KeyboardInterrupt:
                # 處理鍵盤中斷（Ctrl+C）
                print('伺服器結束：鍵盤 Ctrl-C 中斷')
                raise SystemExit
            except Exception as e:
                # 處理一般異常
                print(f'伺服器結束：發生異常，{e}')
                raise SystemExit
            except SystemExit as e:
                # 處理系統退出
                print(f'伺服器結束：SystemExit，{e}')
                raise
            except:
                # 處理其他未知錯誤
                print('伺服器結束：發生未知錯誤')
                raise SystemExit
            finally:
                # 伺服器結束時的清理工作
                print('網站伺服器結束 ⌛')

def main():
    """主函數：初始化系統並啟動伺服器"""
    global capture
    
    # 初始化影片擷取來源
    if args.video:
        # 使用影片檔案
        capture = cv2.VideoCapture(args.video)
        print(f'使用影片檔案：{args.video}')
    else:
        # 使用預設攝影機（通常為鏡頭索引 0）
        capture = cv2.VideoCapture(0)
        print('使用預設攝影機')
    
    # 設定影像解析度
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    try:
        # 建立並啟動 HTTP 伺服器
        # 參數1: 伺服器地址（空字串表示本機所有介面）
        # 參數2: 連接埠號（9090）
        # 參數3: 請求處理器類別
        server = HTTPServer(('', 9090), CamHandler)
        print('伺服器已啟動，請用瀏覽器開啟 http://localhost:9090/a.mjpg 👀')
        print('提示：可按 Ctrl+C 中斷伺服器')
        
        # 開始服務（持續運行直到中斷）
        server.serve_forever()
        
    except KeyboardInterrupt:
        # 處理鍵盤中斷
        print('程式結束：鍵盤 Ctrl-C 中斷')
    except Exception as e:
        # 處理一般異常
        print(f'程式結束：發生異常，{e}')
    except SystemExit as e:
        # 處理系統退出
        print(f'程式結束：SystemExit，{e}')
    except:
        # 處理其他未知錯誤
        print('程式結束：發生未知錯誤')
    finally:
        # 程式結束時的清理工作
        capture.release()        # 釋放影片擷取資源
        server.socket.close()    # 關閉伺服器 Socket
        print('程式結束，資源已釋放')

# 程式進入點
if __name__ == '__main__':
    main()

# 參考來源：https://github.com/berak/opencv_smallfry/blob/master/mjpg_serve.py
# 功能擴展建議：
# 1. 可加入解析度參數（-w 寬度, -h 高度）
# 2. 可加入影片循環次數參數
# 3. 可加入品質參數控制 JPEG 壓縮品質
