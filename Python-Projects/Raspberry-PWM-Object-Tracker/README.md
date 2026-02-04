# 樹莓派人臉辨識與物體追蹤系統

一個基於樹莓派、OpenCV 和 PWM 控制的智慧攝影機系統，具備人臉辨識、物體偵測和自動追蹤功能。

## 🎯 功能特色
- **多人臉辨識**：識別已知人員並標記陌生人
- **物體偵測**：支援 20 種 MobileNetSSD 物體類別偵測
- **自動追蹤**：根據偵測目標自動調整攝影機角度
- **即時串流**：HTTP 串流伺服器供遠端觀看
- **PWM 控制**：精準控制伺服馬達角度
- **Docker 支援**：容器化部署，方便移植

## 📊 支援的物體類別
\`\`\`python
# MobileNetSSD 支援的 20 個類別：
1: aeroplane, 2: bicycle, 3: bird, 4: boat, 5: bottle
6: bus, 7: car, 8: cat, 9: chair, 10: cow
11: diningtable, 12: dog, 13: horse, 14: motorbike
15: person, 16: pottedplant, 17: sheep, 18: sofa
19: train, 20: tvmonitor
\`\`\`

## 🚀 快速開始

### 硬體需求
- 樹莓派 (Raspberry Pi)
- USB 攝影機
- SG90 伺服馬達
- PCA9685 PWM 擴展板 (可選)

### 軟體需求
- Python 3.7+
- OpenCV 4.5+
- Docker (可選)

### 安裝步驟

\`\`\`bash
# 1. 克隆專案
git clone <your-repo-url>
cd Raspberry-PWM-Object-Tracker

# 2. 安裝依賴套件
pip install -r requirements.txt

# 3. 安裝 pigpio
sudo apt-get install pigpio python-pigpio python3-pigpio

# 4. 啟動 pigpio daemon
sudo systemctl start pigpiod
\`\`\`

### 基礎使用

\`\`\`bash
# 1. 啟動陌生人偵測與臉部辨識
python src/main/stranger.py

# 2. 偵測特定物體 (例如：狗)
python src/main/search_xx_rec.py -o 12

# 3. 播放錄製的影片
python src/main/vplay.py -v output/output.mp4 -s 20

# 4. 單純臉部偵測
python src/main/search_face.py
\`\`\`

## 📁 專案結構
\`\`\`
Raspberry-PWM-Object-Tracker/
├── README.md              # 主說明文件
├── README.en.md           # 英文說明
├── requirements.txt       # Python 依賴套件
├── .gitignore            # Git 忽略檔案
├── docs/                 # 技術文件
│   ├── SETUP_GUIDE.md    # 完整安裝指南
│   ├── DOCKER_SETUP.md   # Docker 部署指南
│   └── HARDWARE_SETUP.md # 硬體接線指南
├── src/                  # 原始碼
│   ├── main/            # 主程式
│   │   ├── stranger.py   # 陌生人偵測主程式
│   │   ├── search_xx_rec.py # 物體偵測程式
│   │   ├── search_face.py  # 臉部偵測程式
│   │   ├── vplay.py      # 影片播放器
│   │   ├── myCam1.py     # 多線程攝影機類別
│   │   ├── myCam0.py     # 基礎攝影機類別
│   │   └── myPWM.py      # PWM 控制模組
│   └── utils/           # 工具函數
├── models/              # 機器學習模型
│   ├── MobileNetSSD_deploy.prototxt
│   ├── MobileNetSSD_deploy.caffemodel
│   ├── deploy.prototxt.txt
│   └── res10_300x300_ssd_iter_140000.caffemodel
├── img/                 # 臉部辨識參考圖片
│   ├── Co-p.jpg
│   ├── chinese.jpg
│   └── english.jpg
├── scripts/            # 腳本檔案
├── tests/             # 測試程式
├── examples/          # 使用範例
└── output/            # 輸出檔案 (錄影)
\`\`\`
