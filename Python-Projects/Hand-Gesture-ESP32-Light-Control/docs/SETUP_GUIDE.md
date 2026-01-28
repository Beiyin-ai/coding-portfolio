# 完整設定指南

## 📋 專案概述
此專案使用 MediaPipe 手部辨識技術，偵測剪刀、石頭、布手勢，並透過 Jetson Nano 控制 ESP32 上的 WS2812 全彩燈條。

## 🛠 硬體需求清單
- Jetson Nano 開發板
- ESP32 Wrover Module 開發板
- WS2812 RGB LED 燈條 (8顆)
- USB 網路攝影機
- USB 轉 TTL 序列線 (CH340/CH341 晶片)
- 杜邦線 (公對公、公對母)
- 5V/3A 電源供應器 (供電給 LED 燈條)

## 🔌 硬體接線圖

### Jetson Nano ↔ ESP32 序列通訊


### ESP32 ↔ WS2812 LED 燈條


## ⚙️ 軟體環境設定

### 步驟 1：安裝相依套件


### 步驟 2：序列埠權限設定
根據你的 dmesg 輸出，USB 序列裝置為 `/dev/ttyUSB0`：



### 步驟 3：測試序列埠連線


## 🔧 ESP32 韌體上傳

### 使用 Arduino IDE
1. 安裝 Arduino IDE
2. 安裝 ESP32 開發板支援：
   - 檔案 → 偏好設定 → 附加開發板管理員網址
   - 新增: `https://espressif.github.io/arduino-esp32/package_esp32_index.json`
3. 工具 → 開發板 → ESP32 Wrover Module
4. 安裝 Adafruit NeoPixel 函式庫：
   - 工具 → 管理程式庫 → 搜尋 "Adafruit NeoPixel" → 安裝
5. 開啟 `esp32/firmware.ino`
6. 選擇正確的序列埠
7. 點選上傳按鈕

### 使用 PlatformIO (VSCode)
1. 安裝 PlatformIO IDE 擴充
2. 開啟專案資料夾
3. 編譯並上傳

## 🚀 執行專案

### 方法一：使用執行腳本


### 方法二：手動執行


## 📊 手勢對應表

| 手勢 | 代碼 | LED 顏色 | 顏色代碼 |
|------|------|----------|----------|
| 布 (Paper) | 1 | 白色 | `#ffffff` |
| 石頭 (Rock) | 2 | 綠色 | `#33ff33` |
| 剪刀 (Scissors) | 3 | 紅色 | `#ff0000` |
| 未知/無手 | 4 | 熄滅 | `#000000` |

## 🐛 常見問題排除

### Q1: 出現 "Permission denied" 錯誤
**解決方法：**


### Q2: 找不到序列埠 `/dev/ttyUSB0`
**解決方法：**
1. 檢查 USB 線是否確實連接
2. 執行 `dmesg | grep tty` 查看系統偵測記錄
3. 重新插拔 USB 轉 TTL 線

### Q3: ESP32 LED 不亮
**檢查清單：**
1. 確認電源供應足夠 (5V/3A)
2. 檢查 GPIO 33 是否正確連接至 LED 的 DIN
3. 確認所有接地 (GND) 連接在一起
4. 檢查韌體是否成功上傳

### Q4: 手勢辨識不準確
**調整方法：**
1. 確保手部在畫面中央，光線充足
2. 修改 `main.py` 中的辨識參數：
   - 增加 `min_detection_confidence` (例如: 0.7)
   - 降低 `model_complexity` (設定為 0)
3. 調整手勢姿勢，保持手部穩定

## 📁 專案目錄結構
├── README.en.md                 # 英文說明
├── requirements.txt             # Python 相依套件
├── setup.sh                     # 安裝腳本
├── run.sh                       # 執行腳本
├── jetson/                      # Jetson Nano 程式
│   ├── main.py                  # 主程式
│   └── utils.py                 # 工具函式
├── esp32/                       # ESP32 韌體
│   ├── firmware.ino             # Arduino 程式
│   └── README.md                # ESP32 說明
├── docs/                        # 文件
│   ├── SETUP_GUIDE.md           # 本文件
│   ├── SERIAL_SETUP.md          # 序列埠設定
│   └── TROUBLESHOOTING.md       # 故障排除
└── tests/                       # 測試程式
    └── test_serial.py           # 序列通訊測試


## 📞 技術支援
- 查看詳細故障排除：`docs/TROUBLESHOOTING.md`
- 序列埠設定詳解：`docs/SERIAL_SETUP.md`
- 執行測試程式：`python3 tests/test_serial.py`

---
**更新日期：** 2024年1月
**專案狀態：** ✅ 可運作
