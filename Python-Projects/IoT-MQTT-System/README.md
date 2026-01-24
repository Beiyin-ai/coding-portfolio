# IoT MQTT 訊息傳遞系統

一個完整的 Docker 化 MQTT 訂閱者系統實作專案，基於謝燿聰老師的物聯網通訊實務課程教材。

## 🎯 專案特色

✅ **完整實作** - 包含 MQTT 訂閱者、發布者完整實作
✅ **容器化部署** - 使用 Docker 容器化技術，易於部署
✅ **實際測試** - 已實際在 Ubuntu 環境測試驗證
✅ **完整文件** - 包含詳細的執行說明和架構文件
✅ **教學導向** - 基於課程教材，適合學習參考

## 📁 專案結構

```
IoT-MQTT-System/
├── README.md                 # 中文說明文件
├── .gitignore                # Git 忽略設定
├── requirements.txt          # Python 套件清單
├── Dockerfile                # Docker 建置檔
├── appRun.sh                 # 容器啟動腳本
├── subscriber.py             # 基本訂閱者程式
├── tmp-sub.py                # 進階訂閱者程式
├── publisher.py              # 發布者程式
├── run-instructions.txt      # 完整執行說明
├── setup.sh                  # 一鍵安裝腳本
└── docs/                     # 文件目錄
    └── ARCHITECTURE.md       # 系統架構說明
```

## 🚀 快速開始

### 方法一：最簡單的方式（使用 setup.sh）
```bash
# 給予執行權限
chmod +x setup.sh

# 執行安裝腳本
./setup.sh
```

### 方法二：手動安裝
```bash
# 1. 安裝 Python 套件
pip install -r requirements.txt

# 2. 啟動 MQTT Broker
docker run -d -p 1883:1883 --name mqtt_broker eclipse-mosquitto

# 3. 執行訂閱者
python subscriber.py

# 4. 發布測試訊息（另一終端機）
python publisher.py
```

### 方法三：使用 Docker 容器化執行
```bash
# 1. 建置映像檔
docker build -t iot_mqtt:112 .

# 2. 執行容器
docker run -d \
    --name iot_mqtt \
    --restart unless-stopped \
    -v $(pwd):/x \
    -v ~/log_mqtt:/xlog_mqtt \
    iot_mqtt:112
```

## 📚 學習重點

1. **MQTT 通訊協定**：理解發布/訂閱模式
2. **Python MQTT 程式設計**：使用 paho-mqtt 套件
3. **Docker 容器化**：應用程式容器化部署
4. **系統整合**：MQTT + HTTP 數據傳輸
5. **實務操作**：終端機命令與 Python 程式測試

## 👩‍💻 作者

**邱佩吟**
- 課程：物聯網通訊實務
- 教師：謝燿聰老師
- 完成日期：2026年1月

## 📄 授權

本專案僅供學習參考，基於課程教材改編。
