# 樹莓派人臉辨識與物體追蹤系統

一個基於樹莓派、OpenCV 和 PWM 控制的智慧攝影機系統，具備人臉辨識、物體偵測和自動追蹤功能。本專案結合了電腦視覺與硬體控制，實現了智慧監控與互動應用。

**⚠️ 重要聲明：本專案僅供學術研究與教育目的使用，使用時請遵守當地隱私權法規。**

## 🎯 功能特色

### 臉部辨識與偵測
- **多人臉辨識**：識別已知人員並標記陌生人
- **即時臉部偵測**：使用 OpenCV DNN 模型快速偵測臉部
- **臉部比對**：比對已知臉部資料庫，實現身份識別

### 物體偵測與追蹤
- **20 種物體偵測**：支援 MobileNetSSD 20 個物件類別
- **自動追蹤**：根據偵測目標自動調整攝影機角度
- **物體分類**：可指定偵測特定物件（如狗、貓、汽車等）

### 系統功能
- **即時串流**：HTTP 串流伺服器供遠端觀看（MJPG 格式）
- **PWM 控制**：精準控制伺服馬達角度，實現雲台追蹤
- **Docker 支援**：容器化部署，方便移植與測試
- **錄影功能**：偵測到陌生人或特定物件時自動錄影

## 📊 支援的物體類別

```python
# MobileNetSSD 支援的 20 個類別：
1: 飛機 (aeroplane)     2: 自行車 (bicycle)     3: 鳥 (bird)     4: 船 (boat)     5: 瓶子 (bottle)
6: 巴士 (bus)           7: 汽車 (car)           8: 貓 (cat)      9: 椅子 (chair)  10: 牛 (cow)
11: 餐桌 (diningtable)  12: 狗 (dog)            13: 馬 (horse)   14: 摩托車 (motorbike)  15: 人 (person)
16: 盆栽 (pottedplant)  17: 羊 (sheep)          18: 沙發 (sofa)  19: 火車 (train)  20: 電視 (tvmonitor)
```

## 🚀 快速開始

### 硬體需求
- **樹莓派** (Raspberry Pi 3B+ 或更高版本，建議 4B)
- **USB 攝影機** (支援 Linux UVC driver)
- **SG90 伺服馬達** (用於控制攝影機角度)
- **PCA9685 PWM 擴展板** (可選，用於多馬達控制)
- **電源供應** (5V 3A 以上)

### 軟體需求
- Python 3.7+
- OpenCV 4.5+
- Docker (可選，用於容器化部署)

### 安裝步驟

#### 1. 基本安裝
```bash
# 克隆專案
git clone https://github.com/你的用戶名/Raspberry-PWM-Object-Tracker.git
cd Raspberry-PWM-Object-Tracker

# 安裝 Python 依賴
pip install -r requirements.txt

# 安裝 pigpio (PWM 控制)
sudo apt-get install pigpio python-pigpio python3-pigpio
sudo systemctl start pigpiod
sudo systemctl enable pigpiod
```

#### 2. 下載模型檔案
```bash
# 下載 MobileNetSSD 模型
wget -P models/ https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/deploy.prototxt
wget -P models/ https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/mobilenet_iter_73000.caffemodel
mv models/deploy.prototxt models/MobileNetSSD_deploy.prototxt
mv models/mobilenet_iter_73000.caffemodel models/MobileNetSSD_deploy.caffemodel

# 下載臉部偵測模型
wget -P models/ https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
wget -P models/ https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel
```

#### 3. 準備臉部圖片
將要辨識的臉部圖片放入 `img/` 目錄：
- `xxx.jpg`
- `xxx.jpg`
- `xxx.jpg`

## 📁 專案結構

```
Raspberry-PWM-Object-Tracker/
├── README.md              # 專案說明文件
├── README.en.md           # 英文說明文件
├── requirements.txt       # Python 依賴套件
├── docs/                  # 技術文檔
│   ├── DOCKER_SETUP.md   # Docker 部署指南
│   └── docker-usage.md   # Docker 使用說明
├── img/                   # 臉部辨識圖片
│   └── README.md         # 圖片說明
└── src/                   # 原始碼
    ├── stranger.py       # 陌生人偵測主程式
    ├── search_xx_rec.py  # 物體偵測程式
    ├── search_face.py    # 臉部偵測程式
    ├── vplay.py          # 影片播放器
    ├── myCam1.py         # 多線程攝影機類別
    ├── myCam0.py         # 基礎攝影機類別
    └── myPWM.py          # PWM 控制模組
```

## 🚪 使用方式

### 1. 陌生人偵測
```bash
cd src
python stranger.py
```

### 2. 偵測特定物體
```bash
cd src
# 偵測狗
python search_xx_rec.py -o 12

# 偵測貓
python search_xx_rec.py -o 8

# 偵測汽車
python search_xx_rec.py -o 7
```

### 3. 臉部偵測
```bash
cd src
python search_face.py
```

### 4. 播放錄製影片
```bash
cd src
python vplay.py -v ../output/output.mp4

# 設定播放速度（每 0.2 秒一畫面）
python vplay.py -v ../output/output.mp4 -s 20
```

## 🐳 Docker 部署

### 快速執行
```bash
# 偵測狗
docker run -it --rm -v /dev:/dev --privileged \
  -v /etc/localtime:/etc/localtime:ro \
  -e "LANG=C.UTF-8" \
  -p 9090:9090 \
  -v $(pwd):/app \
  -w /app/src \
  cv2-ocr-lcd-gpio-fr:cv3.3 python search_xx_rec.py -o 12
```

詳細 Docker 使用說明請參考 [docs/DOCKER_SETUP.md](docs/DOCKER_SETUP.md)。

## 🔧 設定調整

### 追蹤靈敏度
在 `stranger.py` 或 `search_xx_rec.py` 中調整以下參數：

```python
ADJ_DIFF = 80      # 觸發調整的像素差異（預設：80）
ADJ_STEP = 1       # 每次調整的角度步進（預設：1）
CONFIDENCE = 0.6   # 偵測信賴度閾值（預設：0.6）
SKIPFLAME = 1      # 調整後的跳過幀數（預設：1）
```

### 攝影機解析度
在 `myCam1.py` 中調整：

```python
# 較低解析度，效能較好
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 較高解析度，畫質較好
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```

## 📝 使用範例

### 範例 1：教室監控
```bash
# 監控教室，識別老師與學生
cd src
python stranger.py

# 在瀏覽器開啟
# http://樹莓派IP:9090/a.mjpg
```

### 範例 2：寵物監視器
```bash
# 偵測家中的寵物
cd src
python search_xx_rec.py -o 12  # 狗
python search_xx_rec.py -o 8   # 貓
```

### 範例 3：停車場車輛偵測
```bash
# 偵測進出車輛
cd src
python search_xx_rec.py -o 7   # 汽車
```

## 🛠️ 故障排除

### 問題 1：找不到攝影機
```
錯誤：capture.isOpened(): False
解決：
1. 檢查攝影機是否正確連接
2. 檢查 /dev/video* 權限：sudo chmod 666 /dev/video0
3. 將使用者加入 video 群組：sudo usermod -a -G video $USER
```

### 問題 2：PWM 連線失敗
```
錯誤：無法連線到 pigpio daemon
解決：
1. 確認 pigpiod 服務已啟動：sudo systemctl status pigpiod
2. 檢查防火牆設定
3. Docker 環境確認正確的 IP（預設：172.17.0.1:8888）
```

### 問題 3：模型檔案缺失
```
錯誤：無法載入模型檔案
解決：
1. 確認 models/ 目錄有正確的檔案
2. 下載缺失的模型檔案（參考安裝步驟 2）
3. 檢查檔案權限
```

## 🌐 語言版本
- [中文版本](README.md)
- [English Version](README.en.md)

---

**注意**：使用時請遵守當地隱私權法規，尊重他人隱私。僅供學術研究與教育目的使用。
