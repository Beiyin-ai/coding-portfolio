# API 文件

## 接收數據
- **URL**: `POST /api/sensor-data`
- **Body**: JSON
```json
{
  "device_id": "ESP32_01",
  "timestamp_esp": 12345,
  "solar_voltage": 5.2,
  "power": {
    "bus_voltage": 5.02,
    "current_ma": 120,
    "power_mw": 604
  },
  "environment": {
    "temperature_c": 25.3,
    "humidity_percent": 60.5,
    "illuminance_raw": 2048
  }
}
\`\`\`

## 查詢最新數據
- **URL**: `GET /api/latest`

## 查詢歷史數據
- **URL**: `GET /api/history?hours=24&device=ESP32_01`
