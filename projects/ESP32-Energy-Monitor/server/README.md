# 能源監控系統 - Flask API 伺服器

基於 Flask 和 MySQL 的物聯網能源監控系統後端 API，負責接收 ESP32 上傳的感測器數據並提供查詢接口。

## 📊 功能

- 接收 ESP32 感測器數據（用電量、溫度、濕度、光照、太陽能）
- 儲存到 MySQL 資料庫
- 提供 RESTful API 查詢數據
- 模組化設計，易於維護和擴展
- 自動初始化資料庫表格和索引

## 🚀 快速開始

### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

### 2. 設定資料庫

編輯 `config.py`，設定 MySQL 連線資訊：

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'energy_monitor',
    'charset': 'utf8mb4'
}
```

### 3. 啟動伺服器

```bash
python app.py
```

伺服器將運行在 `http://localhost:5000`

## 📡 API 端點

| 方法 | 端點 | 說明 |
|------|------|------|
| GET | `/api/` | API 狀態 |
| POST | `/api/sensor-data` | 接收 ESP32 數據 |
| GET | `/api/latest` | 取得最新 10 筆數據 |
| GET | `/api/history` | 查詢歷史數據 |

### 接收數據範例

```json
{
  "device_id": "ESP32_01",
  "timestamp_esp": 1234567890,
  "solar_voltage": 3.2,
  "power": {
    "bus_voltage": 5.0,
    "shunt_voltage": 0.1,
    "load_voltage": 5.1,
    "current_ma": 150,
    "power_mw": 750
  },
  "environment": {
    "temperature_c": 25.3,
    "humidity_percent": 60.5,
    "illuminance_raw": 2048
  }
}
```

### 查詢範例

```bash
# 取得最新數據
curl http://localhost:5000/api/latest

# 查詢最近 48 小時數據
curl http://localhost:5000/api/history?hours=48
```

## 📁 專案結構

```
server/
├── app.py                 # 主程式
├── config.py              # 設定檔
├── requirements.txt       # 套件清單
├── .gitignore             # Git 忽略檔案
├── database/
│   ├── __init__.py
│   ├── db_connection.py   # 資料庫連線
│   └── models.py          # SQL 查詢
└── api/
    ├── __init__.py
    └── routes.py          # API 路由
```

## 🔧 技術棧

- Flask 3.1.3
- MySQL 8.0
- mysql-connector-python 9.6.0

## 📝 License

MIT
