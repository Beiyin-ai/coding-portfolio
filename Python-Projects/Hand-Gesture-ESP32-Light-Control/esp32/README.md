# ESP32 韌體說明

## 硬體接線

### 序列通訊 (Jetson Nano ↔ ESP32)
- ESP32 RX (GPIO 16) ← Jetson Nano TX (Pin 8)
- ESP32 TX (GPIO 17) → Jetson Nano RX (Pin 10) (可選，用於除錯)
- GND ↔ GND

### LED 燈條 (ESP32 ↔ WS2812)
- ESP32 GPIO 33 → WS2812 數據線 (DIN)
- ESP32 5V → WS2812 5V
- ESP32 GND → WS2812 GND

## 上傳步驟

### 方法一：使用 Arduino IDE
1. 安裝 Arduino IDE
2. 安裝 ESP32 開發板支援
   - 檔案 → 偏好設定 → 附加開發板管理員網址
   - 新增: `https://espressif.github.io/arduino-esp32/package_esp32_index.json`
3. 工具 → 開發板 → ESP32 Wrover Module
4. 安裝 Adafruit NeoPixel 函式庫
   - 工具 → 管理程式庫 → 搜尋 "Adafruit NeoPixel" → 安裝
5. 開啟 `firmware.ino`
6. 選擇正確的序列埠
7. 點選上傳按鈕

### 方法二：使用 PlatformIO (VSCode 擴充)
1. 安裝 PlatformIO IDE 擴充
2. 開啟專案資料夾
3. 編譯並上傳

## 除錯
- 開啟序列埠監視器 (波特率 9600)
- 查看收到的代碼和 LED 狀態

## 注意事項
- 確保電源足夠供應 LED 燈條
- 建議使用外部 5V 電源供應 LED
- 資料線需連接 330-470Ω 電阻以防止損壞
