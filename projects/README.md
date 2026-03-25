# Projects 專案專區

本目錄存放完整的軟體專案，展示綜合技術能力與問題解決能力。

## 🎯 專案理念
結合軟體開發與硬體整合能力，解決實際產業問題，
建立從概念到原型的完整解決方案。

## 📂 專案列表

### 1. [**ESP32 太陽能能源監控系統**](./ESP32-Energy-Monitor/)
太陽能發電監測與數據可視化系統

**狀態**：🟢 已完成 (v1.1.0)
**技術**：ESP32 + INA219 + DHT22 + OLED + Flask + MySQL

#### ✨ 功能特色
- 📊 **即時監控**：電壓、電流、功率、溫度、濕度、光照、太陽能電壓
- 🌐 **資料上傳**：WiFi 傳輸到 Flask 後端伺服器，存入 MySQL 資料庫
- 📟 **本地顯示**：OLED 螢幕顯示即時數據
- 💡 **功率實驗設計**：LED 固定為粉紅色，確保功率測量一致性
- 🔧 **模組化設計**：程式碼分工明確，易於維護與擴充
- 🧪 **完整測試**：8 個獨立測試程式，確保每個元件正常運作

#### 📁 專案結構
```
ESP32-Energy-Monitor/
├── firmware/          # ESP32 主程式
├── server/            # Flask 後端 (app.py)
├── database/          # MySQL 資料庫結構
├── docs/              # 說明文件（接線圖、API、LED 說明）
└── tests/             # 8 個元件測試程式
```

#### 🔗 相關連結
- [硬體接線圖](./ESP32-Energy-Monitor/docs/hardware_wiring.md)
- [API 文件](./ESP32-Energy-Monitor/docs/api_docs.md)
- [LED 顏色說明](./ESP32-Energy-Monitor/docs/led_color_meaning.md)

---

### 2. [**ESP32 智慧桌面顯示器**](./ESP32-Smart-Desktop-Display/)
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
├── firmware/   # MicroPython 韌體
├── docs/       # 說明文件
└── tools/      # 工具腳本
```

---

## 🔄 專案狀態總覽

| 專案 | 狀態 | 完成度 | 最後更新 |
|------|------|--------|----------|
| ESP32 太陽能監控系統 | 🟢 已完成 | 100% | 2025-03-25 |
| ESP32 智慧桌面顯示器 | 🟡 開發中 | 40% | 2024-03-19 |

## 🏆 技術亮點

- **嵌入式系統**：ESP32、Arduino、MicroPython
- **感測器整合**：INA219、DHT22、光敏電阻、太陽能板
- **顯示技術**：OLED、ST7789、WS2812 LED
- **後端開發**：Python Flask、RESTful API
- **資料庫**：MySQL
- **通訊協定**：WiFi、HTTP、I2C

## 📊 統計數據

- **專案總數**：2 個
- **程式語言**：C++、Python、MicroPython
- **感測器類型**：5+ 種
- **測試程式**：8+ 個

---

*從感測器到雲端，從概念到原型*
