# 故障排除指南

## 🚨 快速問題診斷流程



## 🔧 硬體問題

### 問題：序列埠無法開啟

**症狀：**
- 程式輸出：`序列埠開啟失敗`
- 錯誤訊息：`Permission denied` 或 `could not open port`

**解決步驟：**
1. **檢查裝置連接：**
   ```bash
   # 確認 USB 裝置被偵測到
   lsusb | grep -i ch341
   # 應該顯示：Bus 001 Device 006: ID 1a86:7523 QinHeng Electronics CH341 serial converter
   ```

2. **檢查裝置路徑：**
   ```bash
   # 查看所有序列埠
   ls -la /dev/tty*
   # 應該看到 /dev/ttyUSB0
   ```

3. **設定權限：**
   ```bash
   # 方法 1: 暫時解決
   sudo chmod 666 /dev/ttyUSB0

   # 方法 2: 永久解決
   sudo usermod -a -G dialout $USER
   # 登出後重新登入
   ```

4. **檢查裝置占用：**
   ```bash
   # 查看是否有其他程式使用序列埠
   sudo lsof /dev/ttyUSB0
   ```

### 問題：LED 燈條不亮

**症狀：**
- 手勢辨識正常，但 LED 無反應
- ESP32 通訊正常，但 LED 不亮

**解決步驟：**
1. **檢查電源：**
   - WS2812 需要穩定 5V 電源
   - 每顆 LED 全亮時約需 60mA
   - 8顆 LED 全亮需約 480mA
   - 建議使用外部 5V/3A 電源

2. **檢查接線：**
   - ESP32 GPIO 33 → LED DIN (數據輸入)
   - 5V → LED 5V (建議外接電源)
   - GND → LED GND (必須共地)

3. **測試單顆 LED：**
   ```python
   # 簡化測試程式
   import serial
   import time
   
   ser = serial.Serial('/dev/ttyUSB0', 9600)
   
   # 測試每種顏色
   for code in ['1', '2', '3', '4']:
       ser.write(f'{code}\n'.encode())
       print(f'發送代碼: {code}')
       time.sleep(2)
   ```

4. **檢查數據線電阻：**
   - 在 GPIO 33 和 DIN 之間串接 330-470Ω 電阻
   - 防止電壓突波損壞 LED

## 🖥 軟體問題

### 問題：鏡頭無法開啟

**症狀：**
- 程式輸出：`無法讀取影像`
- 畫面黑屏或停滯

**解決步驟：**
1. **檢查鏡頭編號：**
   ```python
   # 測試不同鏡頭編號
   import cv2
   
   for i in range(0, 4):
       cap = cv2.VideoCapture(i)
       if cap.isOpened():
           print(f'找到鏡頭: {i}')
           cap.release()
   ```

2. **檢查鏡頭權限：**
   ```bash
   # 查看視訊裝置權限
   ls -la /dev/video*
   
   # 如果需要，設定權限
   sudo chmod 666 /dev/video0
   ```

3. **檢查是否有其他程式占用：**
   ```bash
   # 查看使用視訊裝置的程式
   sudo lsof /dev/video0
   ```

### 問題：手勢辨識不準確

**症狀：**
- 手勢辨識錯誤率高
- 不同手勢被辨識為同一種
- 無手狀態誤判為有手

**解決步驟：**
1. **調整辨識參數：**
   修改 `main.py` 中的 MediaPipe 設定：
   ```python
   with mp_hands.Hands(
       model_complexity=0,           # 0=最快, 1=較準確
       max_num_hands=1,              # 辨識手數
       min_detection_confidence=0.7, # 提高可減少誤判
       min_tracking_confidence=0.5): # 追蹤信度
   ```

2. **調整手勢邏輯：**
   修改 `get_gesture_data` 函式中的判斷條件：
   ```python
   # 原條件
   if total_open >= 4:  # 布
   
   # 可調整為更嚴格條件
   if total_open >= 4 and fingers_open[0] == 1:  # 拇指也要張開
   ```

3. **改善環境條件：**
   - 確保光線充足均勻
   - 背景單純，避免複雜圖案
   - 手部在畫面中央，佔畫面 30-50%
   - 避免快速移動手部

4. **加入手勢訓練：**
   收集手勢樣本，訓練簡單分類器：
   ```python
   # 記錄手勢特徵
   def extract_features(landmarks):
       features = []
       for lm in landmarks:
           features.extend([lm.x, lm.y, lm.z])
       return features
   ```

### 問題：程式效能緩慢

**症狀：**
- 畫面更新緩慢，FPS 低
- Jetson Nano 風扇高速運轉
- 手勢反應延遲

**解決步驟：**
1. **降低解析度：**
   ```python
   # 在 main.py 中降低解析度
   cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)   # 降低寬度
   cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # 降低高度
   ```

2. **減少處理負擔：**
   ```python
   # 降低 MediaPipe 複雜度
   model_complexity=0  # 使用輕量模式
   
   # 降低傳送頻率
   send_interval = 0.2  # 每 0.2 秒傳送一次
   ```

3. **跳幀處理：**
   ```python
   frame_skip = 2  # 每 2 幀處理一次
   frame_count = 0
   
   while cap.isOpened():
       frame_count += 1
       if frame_count % frame_skip != 0:
           continue  # 跳過此幀
   ```

4. **關閉視窗顯示：**
   ```python
   # 測試時關閉畫面顯示可大幅提升效能
   # cv2.imshow('Hand Gesture Control', image)
   ```

## 🔍 診斷工具與指令

### 系統狀態檢查


### 序列通訊測試


### 鏡頭測試


## 📞 進階支援

### 如果以上方法都無法解決：
1. **檢查專案 Issues：** 查看是否有類似問題
2. **提供詳細資訊：** 執行以下指令並提供輸出：
   ```bash
   # 系統資訊
   uname -a
   python3 --version
   pip list | grep -E "opencv|mediapipe|pyserial"
   
   # 硬體資訊
   lsusb
   dmesg | grep -i "tty\|usb"
   ```

3. **簡化測試：** 將問題拆解測試：
   - 單獨測試序列通訊
   - 單獨測試手勢辨識
   - 單獨測試 LED 控制

---
**最後更新：** 2024年1月
**適用版本：** v1.0
