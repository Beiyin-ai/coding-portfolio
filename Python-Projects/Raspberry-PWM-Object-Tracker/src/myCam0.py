#!/usr/bin/env python3
"""
基礎攝影機操作模組 - Camera Basic Operations Module

此模組提供簡單的攝影機開啟和讀取功能，適合基礎應用場景。
This module provides simple camera opening and reading functions, suitable for basic applications.

功能包含：
Functions include:
1. 自動偵測可用攝影機 (Auto-detect available cameras)
2. 簡化的攝影機讀取 (Simplified camera reading)
3. 基本的錯誤處理 (Basic error handling)
"""

import cv2
import time


def open_camera(vidFrom=0, vidTo=3):
    """
    嘗試開啟攝影機
    Try to open a camera
    
    Args:
        vidFrom (int): 開始嘗試的攝影機編號，預設 0
                      Starting camera index to try, default 0
        vidTo (int): 結束嘗試的攝影機編號，預設 3
                    Ending camera index to try, default 3
    
    Returns:
        cv2.VideoCapture: 成功開啟的攝影機物件
                         Successfully opened camera object
    
    Raises:
        SystemExit: 所有攝影機都無法開啟時
                   When all cameras fail to open
    """
    vidNow = vidFrom  # 當前嘗試的攝影機編號
    
    print("🔍 開始搜尋可用攝影機...")
    print("🔍 Starting camera search...")
    
    while True:
        # 建立攝影機裝置路徑
        # Create camera device path
        video = f"/dev/video{vidNow}"
        print(f"🔧 嘗試: cv2.VideoCapture(\"{video}\")")
        print(f"🔧 Trying: cv2.VideoCapture(\"{video}\")")
        
        try:
            # 嘗試開啟攝影機
            # Try to open camera
            capture = cv2.VideoCapture(video)
            
        except Exception as e:
            # 處理開啟攝影機時的例外
            # Handle exceptions when opening camera
            print(f"❌ 錯誤: {e}")
            print(f"❌ Error: {e}")
        
        else:
            # 檢查攝影機是否成功開啟
            # Check if camera opened successfully
            if capture.isOpened():
                print("✅ 成功開啟攝影機！")
                print("✅ Camera opened successfully!")
                print("📷 capture.isOpened(): True")
                
                # 設定攝影機解析度為 320x240
                # Set camera resolution to 320x240
                capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
                capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
                
                # 顯示設定的解析度
                # Display configured resolution
                width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
                height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
                print(f"📐 解析度設定: {int(width)}x{int(height)}")
                print(f"📐 Resolution set: {int(width)}x{int(height)}")
                
                return capture
            else:
                print("❌ 無法開啟攝影機")
                print("❌ Cannot open camera")
        
        # 決定下一個要嘗試的攝影機編號
        # Determine next camera index to try
        if vidNow == vidTo:
            vidNow = vidFrom  # 回到起始編號
        else:
            vidNow += 1  # 嘗試下一個編號
        
        # 等待一秒後再嘗試
        # Wait one second before trying again
        print("⏳ 等待 1 秒後重試...")
        print("⏳ Waiting 1 second before retry...")
        time.sleep(1)


# 錯誤計數最大值 - 連續讀取失敗次數限制
# Maximum error count - consecutive read failure limit
errCntMax = 5


def read_frame(capture):
    """
    從攝影機讀取一幀畫面
    Read a frame from camera
    
    Args:
        capture (cv2.VideoCapture): 攝影機物件
                                   Camera object
    
    Returns:
        numpy.ndarray: 讀取到的畫面
                      Captured frame
    
    Raises:
        SystemExit: 連續讀取失敗超過限制時
                   When consecutive read failures exceed limit
        KeyboardInterrupt: 使用者中斷時
                          When user interrupts
    """
    errCnt = 0  # 錯誤計數器
    
    try:
        while True:
            # 讀取攝影機畫面
            # Read camera frame
            retval, frame = capture.read()
            
            if retval:
                # 成功讀取畫面
                # Successfully read frame
                return frame
            else:
                # 讀取失敗，增加錯誤計數
                # Read failed, increase error count
                errCnt += 1
                print(f"⚠️ 第 {errCnt} 次讀取失敗")
                print(f"⚠️ Read failure #{errCnt}")
                
                if errCnt >= errCntMax:
                    # 達到最大錯誤次數，拋出例外
                    # Reached maximum error count, raise exception
                    print("❌ 錯誤次數過多，可能是攝影機問題！")
                    print("❌ Too many errors, possible camera issue!")
                    print("💡 建議檢查：")
                    print("💡 Suggestions:")
                    print("  1. 攝影機是否正確連接")
                    print("  1. Check camera connection")
                    print("  2. 攝影機是否被其他程式占用")
                    print("  2. Check if camera is used by another program")
                    print("  3. 嘗試重新插拔攝影機")
                    print("  3. Try reconnecting the camera")
                    raise RuntimeError("攝影機讀取錯誤，請檢查裝置 /dev/video?")
                
                # 短暫等待後重試
                # Wait briefly before retrying
                time.sleep(0.1)
                continue
    
    except KeyboardInterrupt:
        # 處理使用者中斷 (Ctrl+C)
        # Handle user interrupt (Ctrl+C)
        print("🛑 使用者中斷攝影機讀取")
        print("🛑 User interrupted camera reading")
        raise  # 重新拋出中斷例外
    
    except RuntimeError as e:
        # 處理攝影機讀取錯誤
        # Handle camera read errors
        print(f"❌ 攝影機錯誤: {e}")
        print(f"❌ Camera error: {e}")
        raise SystemExit
    
    except Exception as e:
        # 處理其他未知錯誤
        # Handle other unknown errors
        print(f"❌ 未知錯誤: {e}")
        print(f"❌ Unknown error: {e}")
        raise SystemExit


# ============================================================================
# 使用範例 / Usage Example
# ============================================================================

def main():
    """主要測試函數 / Main test function"""
    print("=" * 50)
    print("📹 myCam0.py 測試程式")
    print("📹 myCam0.py Test Program")
    print("=" * 50)
    
    camera = None  # 攝影機物件初始化
    
    try:
        # 1. 開啟攝影機
        # Open camera
        print("\n🔧 步驟 1: 開啟攝影機")
        print("🔧 Step 1: Opening camera")
        camera = open_camera()
        
        # 2. 讀取並顯示幾幀畫面
        # Read and display several frames
        print("\n🔧 步驟 2: 讀取畫面")
        print("🔧 Step 2: Reading frames")
        
        for i in range(10):
            try:
                frame = read_frame(camera)
                height, width = frame.shape[:2]
                print(f"✅ 第 {i+1} 幀: {width}x{height}")
                print(f"✅ Frame {i+1}: {width}x{height}")
                
                # 這裡可以加入畫面處理的程式碼
                # You can add frame processing code here
                
                time.sleep(0.1)  # 控制讀取速度
                
            except KeyboardInterrupt:
                print("\n🛑 測試中斷")
                print("🛑 Test interrupted")
                break
        
        print("\n✅ 測試完成！")
        print("✅ Test completed!")
    
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
        print("=" * 50)


# ============================================================================
# 程式進入點
# Program entry point
# ============================================================================

if __name__ == "__main__":
    # 直接執行此檔案時，執行測試程式
    # When running this file directly, execute test program
    main()