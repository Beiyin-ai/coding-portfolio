#!/usr/bin/env python3
"""
多線程攝影機模組 - Multi-threaded Camera Module

此模組使用獨立執行緒持續讀取攝影機畫面，提升畫面讀取效率。
This module uses a separate thread to continuously read camera frames, improving frame reading efficiency.

特點 / Features:
1. 多線程讀取：避免主程式等待畫面讀取
   Multi-threaded reading: Prevents main program from waiting for frame reading
2. 自動重試機制：攝影機斷線時自動重新嘗試
   Auto-retry mechanism: Automatically retries when camera disconnects
3. 錯誤處理完善：包含各種錯誤情況處理
   Comprehensive error handling: Handles various error scenarios
4. 緩衝機制：避免畫面讀取延遲
   Buffering mechanism: Prevents frame reading delays
"""

import cv2
import threading
import time


class myCam:
    """
    多線程攝影機類別
    Multi-threaded Camera Class
    
    使用獨立執行緒持續讀取攝影機畫面，主程式可以隨時取得最新畫面。
    Uses a separate thread to continuously read camera frames, main program can get the latest frame at any time.
    """
    
    def __init__(self, vidFrom=0, vidTo=3):
        """
        初始化攝影機
        Initialize camera
        
        Args:
            vidFrom (int): 開始嘗試的攝影機編號，預設 0
                          Starting camera index to try, default 0
            vidTo (int): 結束嘗試的攝影機編號，預設 3
                        Ending camera index to try, default 3
        
        Raises:
            SystemExit: 無法開啟任何攝影機時
                       When unable to open any camera
        """
        # 初始化變數
        # Initialize variables
        self.errCntMax = 5           # 最大錯誤次數 / Maximum error count
        self.frame = None            # 當前畫面 / Current frame
        self.retval = False          # 讀取狀態 / Reading status
        self.reading = False         # 讀取執行緒運行狀態 / Reading thread running status
        self.errCnt = 0              # 錯誤計數 / Error count
        self.fmID = 0                # 畫面 ID (讀取執行緒用) / Frame ID (for reading thread)
        self.O_ID = 0                # 畫面 ID (輸出用) / Frame ID (for output)
        
        vidNow = vidFrom             # 當前嘗試的攝影機編號
        video = None                 # 攝影機裝置路徑
        
        print("🔍 開始初始化多線程攝影機...")
        print("🔍 Initializing multi-threaded camera...")
        
        while True:
            try:
                # 如果之前嘗試過其他攝影機，稍作等待
                # If tried other cameras before, wait briefly
                if video is not None:
                    time.sleep(0.5)
                
                # 建立攝影機裝置路徑
                # Create camera device path
                video = f"/dev/video{vidNow}"
                print(f"🔧 嘗試開啟: {video}")
                print(f"🔧 Trying to open: {video}")
                
                # 嘗試開啟攝影機
                # Try to open camera
                self.capture = cv2.VideoCapture(video)
                
            except KeyboardInterrupt:
                # 處理使用者中斷
                # Handle user interrupt
                print("🛑 使用者中斷攝影機初始化")
                print("🛑 User interrupted camera initialization")
                raise SystemExit
                
            except Exception as e:
                # 處理其他例外
                # Handle other exceptions
                print(f"❌ 初始化錯誤: {e}")
                print(f"❌ Initialization error: {e}")
                raise SystemExit
                
            else:
                # 檢查攝影機是否成功開啟
                # Check if camera opened successfully
                if self.capture.isOpened():
                    print("✅ 成功開啟攝影機！")
                    print("✅ Camera opened successfully!")
                    print("📷 啟動多線程讀取...")
                    print("📷 Starting multi-threaded reading...")
                    
                    self.reading = True  # 設定讀取標記
                    
                    # 設定攝影機解析度
                    # Set camera resolution
                    self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
                    self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
                    
                    # 啟動讀取執行緒
                    # Start reading thread
                    server_thread = threading.Thread(target=self.readloop)
                    server_thread.daemon = True  # 設定為守護執行緒
                    server_thread.start()
                    
                    # 等待執行緒開始運行
                    # Wait for thread to start
                    time.sleep(0.5)
                    break
                    
                else:
                    print("❌ 無法開啟攝影機，嘗試下一個...")
                    print("❌ Cannot open camera, trying next...")
            
            # 嘗試下一個攝影機編號
            # Try next camera index
            if vidNow == vidTo:
                vidNow = vidFrom  # 回到起始編號
            else:
                vidNow += 1       # 嘗試下一個編號
    
    def readloop(self):
        """
        讀取執行緒主函數
        Reading thread main function
        
        持續讀取攝影機畫面，直到 reading 標記為 False。
        Continuously reads camera frames until reading flag is False.
        
        Raises:
            SystemExit: 讀取錯誤次數過多時
                       When too many read errors occur
        """
        try:
            print("📹 讀取執行緒開始運行...")
            print("📹 Reading thread started...")
            
            while self.reading:
                # 讀取攝影機畫面
                # Read camera frame
                self.retval, self.frame = self.capture.read()
                
                if self.retval:
                    # 成功讀取畫面
                    # Successfully read frame
                    self.errCnt = 0     # 重置錯誤計數
                    self.fmID += 1      # 增加畫面 ID
                    
                    # 每 100 幀顯示一次狀態
                    # Display status every 100 frames
                    if self.fmID % 100 == 0:
                        print(f"📊 已讀取 {self.fmID} 幀畫面")
                        print(f"📊 Read {self.fmID} frames")
                        
                else:
                    # 讀取失敗
                    # Read failed
                    self.errCnt += 1
                    print(f"⚠️ 讀取失敗次數: {self.errCnt}")
                    print(f"⚠️ Read failures: {self.errCnt}")
                    
                    if self.errCnt >= self.errCntMax:
                        # 達到最大錯誤次數
                        # Reached maximum error count
                        print("❌ 錯誤次數過多，攝影機可能已斷線！")
                        print("❌ Too many errors, camera may be disconnected!")
                        raise RuntimeError("攝影機讀取錯誤，請檢查裝置 /dev/video?")
                    
                    # 短暫等待後繼續嘗試
                    # Wait briefly and continue trying
                    time.sleep(0.1)
                    continue
                    
        except RuntimeError as e:
            # 處理攝影機讀取錯誤
            # Handle camera read errors
            print(f"❌ 讀取執行緒錯誤: {e}")
            print(f"❌ Reading thread error: {e}")
            raise SystemExit
            
        except Exception as e:
            # 處理其他未知錯誤
            # Handle other unknown errors
            print(f"❌ 讀取執行緒未知錯誤: {e}")
            print(f"❌ Reading thread unknown error: {e}")
            raise SystemExit
            
        finally:
            # 確保攝影機資源被釋放
            # Ensure camera resources are released
            self.capture.release()
            print("🌌 攝影機關閉完成")
            print("🌌 Camera closed successfully")
    
    def read(self):
        """
        取得最新畫面
        Get the latest frame
        
        Returns:
            numpy.ndarray: 最新攝影機畫面
                          Latest camera frame
        
        Raises:
            SystemExit: 攝影機讀取錯誤時
                       When camera read error occurs
        """
        # 等待新畫面可用
        # Wait for new frame to be available
        while self.O_ID == self.fmID:
            if self.errCnt >= self.errCntMax:
                print("❌ 攝影機讀取錯誤，無法取得畫面")
                print("❌ Camera read error, cannot get frame")
                raise SystemExit('攝影機讀取錯誤')
            
            # 短暫等待避免 CPU 過度使用
            # Wait briefly to avoid excessive CPU usage
            time.sleep(0.01)
        
        # 更新輸出畫面 ID
        # Update output frame ID
        self.O_ID = self.fmID
        
        # 回傳畫面副本，避免執行緒安全問題
        # Return frame copy to avoid thread safety issues
        return self.frame.copy()
    
    def getProp_W_H(self):
        """
        取得攝影機解析度
        Get camera resolution
        
        Returns:
            tuple: (寬度, 高度) 的元組
                  Tuple of (width, height)
        """
        width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return (width, height)
    
    def release(self):
        """
        釋放攝影機資源
        Release camera resources
        
        停止讀取執行緒並釋放攝影機。
        Stops reading thread and releases camera.
        """
        print("🔄 停止攝影機讀取...")
        print("🔄 Stopping camera reading...")
        
        self.reading = False  # 停止讀取執行緒
        
        # 等待讀取執行緒結束
        # Wait for reading thread to finish
        time.sleep(0.5)
        
        print("✅ 攝影機資源已釋放")
        print("✅ Camera resources released")


# ============================================================================
# 使用範例 / Usage Example
# ============================================================================

def main():
    """主要測試函數 / Main test function"""
    print("=" * 60)
    print("📹 myCam1.py 多線程攝影機測試程式")
    print("📹 myCam1.py Multi-threaded Camera Test Program")
    print("=" * 60)
    
    camera = None  # 攝影機物件初始化
    
    try:
        # 1. 建立攝影機物件
        # Create camera object
        print("\n🔧 步驟 1: 建立多線程攝影機物件")
        print("🔧 Step 1: Creating multi-threaded camera object")
        camera = myCam()
        
        # 2. 取得攝影機解析度
        # Get camera resolution
        width, height = camera.getProp_W_H()
        print(f"\n📐 攝影機解析度: {width}x{height}")
        print(f"📐 Camera resolution: {width}x{height}")
        
        # 3. 讀取並顯示幾幀畫面
        # Read and display several frames
        print("\n🔧 步驟 2: 測試畫面讀取")
        print("🔧 Step 2: Testing frame reading")
        
        for i in range(20):
            try:
                frame = camera.read()
                h, w = frame.shape[:2]
                print(f"✅ 第 {i+1} 幀: {w}x{h}")
                print(f"✅ Frame {i+1}: {w}x{h}")
                
                # 這裡可以加入畫面處理的程式碼
                # You can add frame processing code here
                
                time.sleep(0.05)  # 控制讀取速度
                
            except KeyboardInterrupt:
                print("\n🛑 測試中斷")
                print("🛑 Test interrupted")
                break
        
        print("\n✅ 多線程攝影機測試完成！")
        print("✅ Multi-threaded camera test completed!")
        
    except KeyboardInterrupt:
        print("\n🛑 使用者中斷程式")
        print("🛑 User interrupted program")
        
    except Exception as e:
        print(f"\n❌ 測試失敗: {e}")
        print(f"❌ Test failed: {e}")
        
    finally:
        # 確保攝影機資源被釋放
        # Ensure camera resources are released
        if camera is not None:
            print("\n🔧 釋放攝影機資源...")
            print("🔧 Releasing camera resources...")
            camera.release()
        
        print("\n🎬 程式結束")
        print("🎬 Program ended")
        print("=" * 60)


# ============================================================================
# 程式進入點
# Program entry point
# ============================================================================

if __name__ == "__main__":
    # 直接執行此檔案時，執行測試程式
    # When running this file directly, execute test program
    main()