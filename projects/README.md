# Projects 專案專區

本目錄存放完整的軟體專案，展示綜合技術能力與問題解決能力。

## 🎯 專案理念
結合軟體開發與硬體整合能力，解決實際產業問題，
建立從概念到原型的完整解決方案。

## 📂 專案列表

### 1. [**Industrial Equipment Smart Sensing & Energy Management Kit**](./industrial-smart-sensing/)
工業設備智慧感知與能源管理套件原型

**狀態**：🟡 開發中
**技術**：ESP32 + Flask + Chart.js
**概述**：為傳統工業設備加裝感測器，實現設備狀態監控、能源消耗可視化與數據集中管理。

---

### 2. [**ESP32 太陽能能源監控系統**](./ESP32-Energy-Monitor/)
太陽能發電監測與數據可視化系統

**狀態**：🟢 已完成 (v1.1.0)
**技術**：ESP32 + INA219 + DHT22 + OLED + Flask

#### ✨ 功能特色
- 📊 即時監控：電壓、電流、功率、溫度、濕度、光照
- 🌐 資料上傳：WiFi傳輸到後端伺服器
- 📟 本地顯示：OLED螢幕顯示即時數據
- 💡 功耗實驗：固定LED顏色/亮度研究環境影響
- 🔧 模組化設計：14個檔案分工，易於維護
- 🧪 完整測試：8個測試程式確保每個元件正常

#### 📁 專案結構
```
ESP32-Energy-Monitor/
├── firmware/   # ESP32韌體（模組化設計）
├── server/     # Flask後端
├── database/   # 資料庫結構
├── docs/       # 說明文件
└── tests/      # 8個元件測試程式
```

#### 🔗 相關連結
- [韌體設定說明](./ESP32-Energy-Monitor/firmware/README.md)
- [硬體接線圖](./ESP32-Energy-Monitor/docs/hardware_wiring.md)
- [API文件](./ESP32-Energy-Monitor/docs/api_docs.md)

---

### 3. [**ESP32 智慧桌面顯示器**](./ESP32-Smart-Desktop-Display/)
基於 ESP32 與 MicroPython 的智慧桌面資訊顯示器

**狀態**：🟡 開發中
**技術**：ESP32 + MicroPython + ST7789 + Wi-Fi

#### ✨ 功能特色
- 🕒 即時時鐘：NTP 網路校時
- 🌤️ 天氣顯示：OpenWeatherMap API 整合
- 📅 行事曆：Google Calendar 事件顯示
- 🔔 通知中心：顯示自訂通知訊息
- 📊 系統監控：CPU/記憶體使用率（連線電腦時）

#### 📁 專案結構
```
ESP32-Smart-Desktop-Display/
├── firmware/   # MicroPython韌體
├── docs/       # 說明文件
└── tools/      # 工具腳本
```

---

## 🔄 專案狀態總覽

| 專案 | 狀態 | 完成度 | 最後更新 |
|------|------|--------|----------|
| Industrial Smart Sensing | 🟡 開發中 | 60% | 2024-03-19 |
| ESP32 太陽能監控系統 | 🟢 已完成 | 100% | 2024-03-19 |
| ESP32 智慧桌面顯示器 | 🟡 開發中 | 40% | 2024-03-19 |

## 🏆 技術亮點

- **嵌入式系統**：ESP32、Arduino、MicroPython
- **感測器整合**：INA219、DHT22、光敏電阻
- **顯示技術**：OLED、ST7789
- **後端開發**：Python Flask、RESTful API
- **資料庫**：MySQL、SQLite
- **通訊協定**：WiFi、HTTP

## 📊 統計數據

- **專案總數**：3 個
- **程式語言**：C++、Python、MicroPython
- **感測器類型**：5+ 種
- **測試程式**：8+ 個

---

*從感測器到雲端，從概念到原型*
