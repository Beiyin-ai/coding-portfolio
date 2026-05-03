# ESP32 能源監控系統

這是一個基於 ESP32 的太陽能能源監控系統，包含感測器讀取、資料視覺化與完整測試程式。

## 📁 專案結構

```
ESP32-Energy-Monitor/
├── firmware/          # ESP32 韌體程式碼
│   ├── config.h       # 設定宣告
│   ├── config.cpp     # 設定數值（WiFi帳密、網址）
│   ├── *.h/cpp        # 各模組程式碼
│   └── README.md      # 韌體設定說明
├── server/            # 後端伺服器 (Flask)
│   ├── app.py         # 主程式
│   └── requirements.txt # Python套件
├── database/          # 資料庫結構
│   ├── schema.sql     # 資料表結構
│   └── init.sql       # 初始化資料
├── docs/              # 說明文件
│   ├── hardware_wiring.md  # 硬體接線圖
│   ├── api_docs.md         # API說明
│   ├── led_color_meaning.md # LED狀態說明
│   ├── troubleshooting.md  # 故障排除
│   └── images/         # 圖片資源
└── tests/             # 元件測試程式
    ├── 01_dht22_test.ino    # DHT22測試
    ├── 02_ina219_test.ino   # INA219測試
    ├── 03_ldr_test.ino      # 光敏電阻測試
    ├── 04_oled_test.ino     # OLED測試
    ├── 05_ws2812_test.ino   # LED燈條測試
    ├── 06_ws2812_ina219_test.ino # 綜合測試
    ├── 07_solar_test.ino    # 太陽能板測試
    └── 08_arduino_uno_solar_test.ino # Arduino測試
```

## ✨ 功能特色

- 📊 **即時監控**：讀取電壓、電流、功率、溫度、濕度、光照
- 🌐 **資料上傳**：透過 WiFi 傳送到後端伺服器
- 📟 **OLED顯示**：本地顯示即時數據
- 💡 **LED指示**：粉紅色恆亮（實驗設計固定耗電）
- 🔧 **模組化設計**：程式碼分層管理，易於維護
- 🧪 **完整測試**：每個元件都有獨立的測試程式

## 🚀 快速開始

### 1. 硬體準備
- ESP32開發板
- INA219 電流感測器
- DHT22 溫濕度感測器
- 光敏電阻
- 0.96吋 OLED 螢幕
- WS2812 LED 燈條
- 太陽能板

### 2. 接線方式
請參考 `docs/hardware_wiring.md`

### 3. 韌體設定
請參考 `firmware/README.md` 修改：
- WiFi 帳號密碼
- 伺服器網址
- 腳位定義

### 4. 後端設定
```bash
cd server
pip install -r requirements.txt
python app.py
```

### 5. 資料庫設定
```bash
# 以 MySQL 為例
mysql -u root -p < database/schema.sql
```

### 6. 上傳韌體
- 用 Arduino IDE 開啟 `firmware/energy_monitor_stable.ino`
- 選擇 ESP32 開發板
- 編譯並上傳

## 🧪 測試程式

在 `tests/` 資料夾中有完整的元件測試程式：

| 檔案 | 測試項目 |
|------|----------|
| `01_dht22_test.ino` | DHT22 溫濕度感測器 |
| `02_ina219_test.ino` | INA219 電流/電壓/功率 |
| `03_ldr_test.ino` | 光敏電阻 |
| `04_oled_test.ino` | OLED 顯示器 |
| `05_ws2812_test.ino` | WS2812 LED 燈條 |
| `06_ws2812_ina219_test.ino` | LED + INA219 綜合測試 |
| `07_solar_test.ino` | 太陽能板電壓測試 |
| `08_arduino_uno_solar_test.ino` | Arduino UNO 太陽能測試 |

## 📚 文件導覽

- [韌體設定說明](firmware/README.md) - WiFi、腳位、顏色設定
- [硬體接線圖](docs/hardware_wiring.md) - 接線方式說明
- [API文件](docs/api_docs.md) - 後端 API 說明
- [LED顏色含義](docs/led_color_meaning.md) - LED狀態指示
- [故障排除](docs/troubleshooting.md) - 常見問題解決

## 📊 數據視覺化

系統會上傳以下數據到後端：
- 溫度 (°C)
- 濕度 (%)
- 電流 (mA)
- 負載電壓 (V)
- 功率 (mW)
- 太陽能板電壓 (V)
- 光照強度 (原始值)

## 🤝 貢獻指南

1. Fork 專案
2. 建立您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m '新增某功能'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 📝 版本歷史

- **v1.0.0** (2024-03-19): 初始版本
  - 基本感測器讀取功能
  - WiFi 資料上傳
  - OLED 顯示
  - LED 控制
  - 完整測試程式

## 📄 授權

MIT License

專案連結: [https://github.com/您的帳號/ESP32-Energy-Monitor](https://github.com/您的帳號/ESP32-Energy-Monitor)