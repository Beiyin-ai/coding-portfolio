# ESP32 Smart Desktop Display / ESP32 智能桌面顯示器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: ESP32](https://img.shields.io/badge/Platform-ESP32-green.svg)](https://www.espressif.com/)
[![Framework: MicroPython](https://img.shields.io/badge/Framework-MicroPython-blue.svg)](https://micropython.org/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)

## 📋 專案概述 / Project Overview

這是一個基於 MicroPython 的物聯網桌面顯示器，整合多種感測器和顯示技術，建立一個智能桌面顯示裝置。專案展示 ESP32 Type-C 開發板的實際應用。

This is a MicroPython-based IoT desktop display that integrates multiple sensors and display technologies to create a smart desktop display device. The project demonstrates practical applications of ESP32 Type-C development board.

## ✨ 主要功能 / Features

### 🖥️ 三種顯示模式
1. **日期與環境模式** - 顯示時間、日期、溫濕度
2. **訊息顯示模式** - 顯示 MQTT 接收的訊息
3. **倒數日期模式** - 顯示重要日子的倒數

### 📡 無線通訊
- **WiFi 連接** - 自動連接無線網路
- **NTP 校時** - 自動同步網路時間
- **MQTT 訂閱** - 接收遠端訊息
- **時區支援** - 自動調整為台灣時間 (UTC+8)

### 🎮 使用者互動
- **按鈕控制** - 切換顯示模式
- **自動返回** - 10秒後自動返回主畫面
- **特殊日期動畫** - 生日/紀念日閃爍效果
- **跑馬燈顯示** - 重要訊息跑馬燈效果

## 🛠️ 技術規格 / Technical Specifications

### 硬體 / Hardware
- **微控制器**: ESP32-WROOM-32 (Type-C 接口)
- **顯示器**: SSD1306 OLED 0.96" (128x64, I2C)
- **感測器**: DHT22 溫濕度感測器
- **輸入裝置**: 輕觸按鈕開關
- **通訊**: WiFi 802.11 b/g/n

### 軟體 / Software
- **框架**: MicroPython 1.21.0
- **開發環境**: Thonny IDE / VS Code
- **主要函式庫**: 
  - `ssd1306` - OLED 顯示驅動
  - `dht` - 溫濕度感測器驅動
  - `umqtt.simple` - MQTT 通訊
  - `ntptime` - 網路時間同步

## 🚀 快速開始 / Quick Start

### 1. 準備硬體
```bash
# 參考接線指南
/docs/wiring_guide.md
```

### 2. 安裝開發環境
```bash
# 安裝必要工具
pip install esptool adafruit-ampy

# 或使用 Thonny IDE
# 下載: https://thonny.org
```

### 3. 燒錄 MicroPython
```bash
# 使用工具腳本
cd tools
./flash_micropython.sh /dev/ttyUSB0
```

### 4. 上傳程式
```bash
# 上傳所有檔案
cd tools
./upload_files.sh /dev/ttyUSB0
```

## 📁 專案結構 / Project Structure
```
ESP32-Smart-Desktop-Display/
├── README.md                    # 說明文件
├── LICENSE                      # MIT 授權
├── firmware/                    # MicroPython 程式碼
│   ├── main.py                 # 主程式
│   ├── boot.py                 # 啟動設定
│   ├── requirements.txt        # 依賴列表
│   └── lib/                    # 自定義函式庫
├── docs/                       # 文件
│   ├── wiring_guide.md        # 接線指南
│   ├── micropython_setup.md   # 環境設定
│   ├── BOM.md                 # 材料清單
│   └── images/                # 圖片目錄
└── tools/                      # 工具腳本
    ├── flash_micropython.sh   # 韌體燒錄
    └── upload_files.sh        # 檔案上傳
```

## 🔧 設定說明 / Configuration

### WiFi 設定
編輯 `firmware/main.py`：
```python
ssid = "Your_WiFi_SSID"
password = "Your_WiFi_Password"
```

### MQTT 設定
```python
mqtt_server = "test.mosquitto.org"  # 公共 MQTT 伺服器
topic_sub = b"your/topic"           # 訂閱主題
```

### 特殊日期設定
```python
special_dates = {
    "0113": "Happy Birthday!",      # 1月13日
    "0716": "My Birthday!",         # 7月16日
    "0515": "Anniversary!"          # 5月15日
}
```

## 📸 使用示範 / Usage Demo

### 基本操作
1. **上電啟動** - 自動連接 WiFi 並同步時間
2. **按鈕操作** - 短按切換顯示模式
3. **自動功能** - 10秒後返回主畫面

### MQTT 測試
```bash
# 發送測試訊息
mosquitto_pub -h test.mosquitto.org -t "pei/oled" -m "Hello ESP32!"
```

## 🐛 疑難排解 / Troubleshooting

| 問題 | 解決方法 |
|------|----------|
| 無法連接 WiFi | 檢查 SSID/密碼，確認訊號強度 |
| OLED 無顯示 | 檢查 I2C 接線，確認地址 0x3C |
| DHT22 讀取失敗 | 檢查接線，添加 10kΩ 上拉電阻 |
| 時間不同步 | 確認網路連接，檢查 NTP 伺服器 |
| MQTT 無法接收 | 檢查網路，確認訂閱主題正確 |

## 📄 授權條款 / License
本專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 聯絡資訊 / Contact
- GitHub: [@Beiyin-ai](https://github.com/Beiyin-ai)
- 專案連結: [ESP32-Smart-Desktop-Display](https://github.com/Beiyin-ai/coding-portfolio/tree/main/projects/ESP32-Smart-Desktop-Display)

## 🙏 致謝 / Acknowledgments
- MicroPython 開發團隊
- ESP32 硬體設計
- 開源社群貢獻者

---
**讓你的桌面變得更智能！** 🚀

## 💡 經驗分享 / Lessons Learned

在開發過程中，我們遇到並解決了以下常見問題，這些經驗對 ESP32 和 MicroPython 新手特別有幫助：

### 🪜 常見問題與解決方案

| 問題 | 原因分析 | 解決方案 |
|------|----------|----------|
| **畫面切換邏輯錯誤** | 使用 `screen_mode = 1 - screen_mode` 只能在兩頁間切換 | 改為 `screen_mode = (screen_mode + 1) % 3` 實現三頁循環 |
| **第三頁卡住無回應** | 跑馬燈迴圈中未檢查按鈕輸入，程式卡在迴圈內 | 添加自動返回計時器：10秒後自動返回第一頁 |
| **時間顯示錯誤 (1970年)** | ESP32 沒有 RTC 電池，開機後時間重置 | 整合 NTP 校時：WiFi 連接後自動同步網路時間並調整時區 (+8) |
| **倒數日顯示過去事件** | 顯示 "passed" 或負數天數造成畫面混亂 | 只顯示未來事件，過去事件僅顯示日期 |
| **字體行距不一致** | 不同頁面使用不同行距 (20px vs 16px) | 統一使用 16px 行距，保持版面一致性 |
| **DHT22 讀取失敗** | 缺少上拉電阻或讀取間隔太短 | 添加 10kΩ 上拉電阻，增加讀取間隔時間 |
| **OLED 顯示亂碼** | I2C 通訊不穩定或地址錯誤 | 確認 I2C 地址 (0x3C)，檢查接線品質 |
| **按鈕抖動誤觸** | 機械開關接觸時產生抖動信號 | 添加軟體去抖動 (debounce) 延遲 50ms |

### 🎯 開發心得

1. **ESP32 時間管理**
   - ESP32 沒有硬體 RTC，必須依賴網路校時
   - 開機後優先連接 WiFi 並同步 NTP 時間
   - 台灣時區需手動調整 (+8 小時)

2. **使用者體驗設計**
   - 按鈕操作要有即時視覺回饋
   - 避免使用者卡在任何畫面 (添加自動返回)
   - 保持介面一致性 (字體、行距、佈局)

3. **錯誤處理與穩定性**
   - 所有感測器讀取都要有 try-except 保護
   - 網路操作要有重試機制
   - 顯示緩衝區更新前先清除

4. **硬體注意事項**
   - DHT22 需要 10kΩ 上拉電阻
   - OLED I2C 接線要短且穩固
   - ESP32 的 3.3V 供電要充足

這些經驗來自實際開發過程中的挑戰與解決方案，希望能幫助其他開發者避免類似問題。
