# 手勢辨識 ESP32 燈光控制系統

一個使用 MediaPipe 手部辨識技術，透過 Jetson Nano 控制 ESP32 全彩燈條的智慧互動系統。

## 🎯 功能特色
- **即時手勢辨識**：使用 MediaPipe 準確辨識剪刀、石頭、布手勢
- **硬體整合控制**：透過序列通訊控制 ESP32 全彩燈條
- **即時視覺回饋**：畫面顯示辨識結果與燈光狀態
- **跨平台相容**：支援 Jetson Nano、樹莓派、一般 PC
- **完整錯誤處理**：序列埠連接失敗自動進入測試模式

## 🤖 手勢對應燈光
| 手勢 | 代碼 | LED 顏色 | 說明 |
|------|------|----------|------|
| ✋ 布 (Paper) | 1 | 白色 (#ffffff) | 五指張開 |
| ✊ 石頭 (Rock) | 2 | 綠色 (#33ff33) | 握拳 |
| ✌️ 剪刀 (Scissors) | 3 | 紅色 (#ff0000) | 食指中指張開 |
| ❓ 未知/無手 | 4 | 黑色/熄滅 (#000000) | 其他手勢或無手 |

## 🚀 快速開始

### 硬體需求
- Jetson Nano 開發板 或 一般 PC
- ESP32 Wrover Module 開發板
- WS2812 全彩 LED 燈條 (8顆)
- USB 網路攝影機
- USB 轉 TTL 序列線 (CH340/CH341)
- 杜邦線若干

### 安裝步驟

1. **克隆專案與設定權限**
```bash
cd Hand-Gesture-ESP32-Light-Control
chmod +x setup.sh run.sh
```

2. **安裝 Python 相依套件**
```bash
./setup.sh
# 或手動安裝
# pip install -r requirements.txt
```

3. **設定序列埠權限**
```bash
# 將使用者加入序列埠存取群組
sudo usermod -a -G dialout $USER
# 登出後重新登入生效
# 或執行：newgrp dialout
```

### 上傳 ESP32 韌體
1. 使用 Arduino IDE 開啟 `esp32/firmware.ino`
2. 安裝 ESP32 開發板支援
3. 安裝 Adafruit NeoPixel 函式庫
4. 選擇開發板：ESP32 Wrover Module
5. 上傳韌體到 ESP32

### 執行方式

#### 方法一：使用執行腳本
```bash
./run.sh
```

#### 方法二：手動執行
```bash
cd jetson
python3 main.py
```

## 📁 專案結構
```
Hand-Gesture-ESP32-Light-Control/
├── README.md                    # 中文說明文件
├── README.en.md                 # 英文說明文件
├── requirements.txt             # Python 相依套件
├── setup.sh                     # 安裝腳本
├── run.sh                       # 執行腳本
├── jetson/                      # Jetson Nano 程式
│   ├── main.py                  # 主程式 - 手勢辨識
│   └── utils.py                 # 工具函式
├── esp32/                       # ESP32 韌體
│   ├── firmware.ino             # Arduino 程式 - LED 控制
│   └── README.md                # ESP32 硬體說明
├── docs/                        # 詳細文件
│   ├── SETUP_GUIDE.md           # 完整設定指南
│   ├── SERIAL_SETUP.md          # 序列埠設定詳解
│   └── TROUBLESHOOTING.md       # 故障排除指南
└── tests/                       # 測試程式
    ├── test_serial.py           # 序列通訊測試
    └── test_hardware.py         # 硬體連線測試
```

## 🧪 測試與除錯

### 硬體連線測試
```bash
cd tests
python3 test_hardware.py
```

### 序列通訊測試
```bash
cd tests
python3 test_serial.py
```

## 🛠️ 使用技術
- **MediaPipe**：Google 手部辨識框架
- **OpenCV**：電腦視覺與影像處理
- **PySerial**：序列埠通訊控制
- **Adafruit NeoPixel**：WS2812 LED 控制函式庫
- **Arduino Framework**：ESP32 嵌入式開發

## 🎯 學習目標
這個專案展示了：
1. **電腦視覺應用**：MediaPipe 手部辨識實作
2. **嵌入式系統整合**：Jetson Nano 與 ESP32 通訊
3. **序列通訊協議**：UART 序列埠資料傳輸
4. **硬體控制程式**：WS2812 LED 燈條控制
5. **跨平台開發**：Python + Arduino 雙平台協作

## 🔄 未來擴展方向
1. **增加手勢種類**：辨識更多手勢控制指令
2. **加入機器學習**：訓練自訂手勢分類模型
3. **網路通訊**：透過 WiFi 遠端控制燈光
4. **多裝置同步**：控制多個 ESP32 燈條
5. **Web 介面**：建立網頁監控與控制介面

## ⚠️ 注意事項
- 確保 USB 轉 TTL 線正確連接 (TX↔RX 交叉)
- WS2812 LED 需要足夠的 5V 電源供應
- 序列通訊需設定正確的波特率 (9600)
- 手勢辨識效果受光線與背景影響
- 首次使用需設定序列埠權限

## 📝 授權條款
MIT License

---

## 🌐 語言版本
- [中文版本](README.md)
- [English Version](README.en.md)
