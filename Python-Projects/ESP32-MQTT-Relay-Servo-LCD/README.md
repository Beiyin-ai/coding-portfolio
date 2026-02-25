# ESP32 MQTT 智慧家庭控制器

一個基於 ESP32 和 MQTT 協定的物聯網家庭自動化系統，可透過 Linux 主機遠端控制繼電器、伺服馬達，並在 LCD 顯示器上即時顯示訊息。

## 🎯 功能特色
- **MQTT 遠端控制**：透過 MQTT 協定接收指令，支援即時控制
- **繼電器控制**：遠端開關電器設備（支援 H/L 指令）
- **伺服馬達驅動**：精確控制 0-180 度旋轉角度
- **LCD 訊息顯示**：16x2 LCD 顯示器，支援自訂文字訊息
- **WiFi 自動連線**：開機自動連線，具備重試機制
- **NTP 時間同步**：自動同步網路時間，支援時區轉換

## 🖥️ 支援的硬體裝置
- **ESP32 開發板**：核心控制單元
- **繼電器模組**：控制家電開關
- **伺服馬達 SG90**：角度控制應用
- **16x2 I2C LCD**：文字訊息顯示
- **LED 指示燈**：系統狀態顯示

## 🚀 快速開始

### 環境需求
- **硬體**：ESP32 開發板、繼電器、伺服馬達、16x2 I2C LCD
- **軟體**：MicroPython、MQTT Broker（可自行搭建）
- **開發工具**：Thonny / VS Code + Pymakr / 任何文字編輯器

### 安裝步驟

1. **燒錄 MicroPython 至 ESP32**
   ```bash
   esptool.py --port /dev/ttyUSB0 erase_flash
   esptool.py --port /dev/ttyUSB0 write_flash 0x1000 esp32-*.bin
   ```

2. **上傳程式碼至 ESP32**
   - 將 `firmware/` 目錄下的所有檔案上傳至 ESP32
   - 修改 `config.json` 中的 WiFi 和 MQTT 設定

3. **安裝相依套件**
   ```bash
   # ESP32 端（透過 mip 或手動上傳）
   mip install umqtt.robust
   
   # Linux 端（如需執行測試）
   pip install paho-mqtt
   ```

## 📁 專案結構
```
ESP32-MQTT-Relay-Servo-LCD/
├── firmware/              # ESP32 韌體主目錄
│   ├── main.py            # 主程式（MQTT 訂閱 + 硬體控制）
│   ├── config.json        # 設定檔（WiFi、MQTT 設定）
│   ├── lib/               # 第三方函式庫
│   │   ├── lcd_api.py     # LCD API 抽象層
│   │   └── machine_i2c_lcd.py # I2C LCD 驅動
│   └── examples/          # 測試範例
│       ├── test_lcd.py    # LCD 時間顯示測試
│       ├── test_servo.py  # 伺服馬達測試
│       └── test_config.py # 設定檔測試
├── scripts/               # 輔助腳本
│   └── mqtt_commands.md   # MQTT 測試指令
├── docs/                  # 文件說明
│   ├── wiring.md          # 接線說明
│   └── TROUBLESHOOTING.md # 常見問題
├── README.md              # 專案說明文件
└── requirements.txt       # 相依套件清單
```

## 🛠️ 使用技術
- **MicroPython**：ESP32 韌體開發
- **MQTT 協定**：裝置間通訊
- **I2C 通訊協定**：LCD 顯示器控制
- **PWM 脈衝調變**：伺服馬達角度控制
- **NTP 網路時間協定**：自動時間同步

## 📝 設定說明

### `config.json` 設定範例
```json
{
    "mqtt_broker": "你的MQTT Broker IP",
    "mqtt_port": 443,
    "topic_head": "你的主題前綴",
    "topic_servo": "/servo",
    "topic_lcd": "/LCD",
    "topic_relay": "/relay"
}
```

### WiFi 設定
在 `main.py` 中修改：
```python
WiFi_ssid = "你的WiFi名稱"
WiFi_password = "你的WiFi密碼"
```

## 🎯 控制指令範例

```bash
# 控制繼電器（H:開，L:關）
mosquitto_pub -h broker_ip -p 443 -t your_topic/relay -m H

# LCD 顯示訊息
mosquitto_pub -h broker_ip -p 443 -t your_topic/LCD -m "Hello World"

# 控制伺服馬達（0-180度）
mosquitto_pub -h broker_ip -p 443 -t your_topic/servo -m 90
```

## 🔧 常見應用場景
1. **智慧照明**：透過繼電器控制燈具開關
2. **窗簾自動化**：伺服馬達控制窗簾開闔
3. **訊息看板**：LCD 顯示即時資訊或公告
4. **定時控制**：結合 NTP 時間實現定時開關

## 📝 授權條款
MIT License
