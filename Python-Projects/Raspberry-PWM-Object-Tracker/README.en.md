# Raspberry Pi Face Recognition and Object Tracking System

A smart camera system based on Raspberry Pi, OpenCV, and PWM control, featuring face recognition, object detection, and auto-tracking capabilities. This project combines computer vision with hardware control for intelligent monitoring and interactive applications.

**⚠️ Important Notice: This project is for academic research and educational purposes only. Please comply with local privacy regulations when using.**

## 🎯 Features

### Face Recognition & Detection
- **Multi-face Recognition**: Identify known persons and mark strangers
- **Real-time Face Detection**: Fast face detection using OpenCV DNN model
- **Face Matching**: Compare with known face database for identity verification

### Object Detection & Tracking
- **20 Object Categories**: Supports 20 MobileNetSSD object classes
- **Auto-tracking**: Automatically adjusts camera angle based on detected targets
- **Object Classification**: Can detect specific objects (e.g., dog, cat, car)

### System Functions
- **Real-time Streaming**: HTTP streaming server for remote viewing (MJPG format)
- **PWM Control**: Precise servo motor angle control for pan-tilt tracking
- **Docker Support**: Containerized deployment for easy portability and testing
- **Recording Function**: Automatically records when strangers or specific objects are detected

## 📊 Supported Object Classes

```python
# 20 MobileNetSSD supported classes:
1: aeroplane     2: bicycle     3: bird     4: boat     5: bottle
6: bus           7: car         8: cat      9: chair    10: cow
11: diningtable  12: dog        13: horse   14: motorbike    15: person
16: pottedplant  17: sheep      18: sofa    19: train   20: tvmonitor
```

## 🚀 Quick Start

### Hardware Requirements
- **Raspberry Pi** (Raspberry Pi 3B+ or higher, recommended 4B)
- **USB Camera** (supports Linux UVC driver)
- **SG90 Servo Motor** (for camera angle control)
- **PCA9685 PWM Expansion Board** (optional, for multi-motor control)
- **Power Supply** (5V 3A or higher)

### Software Requirements
- Python 3.7+
- OpenCV 4.5+
- Docker (optional, for containerized deployment)

### Installation Steps

#### 1. Basic Installation
```bash
# Clone the project
git clone https://github.com/your-username/Raspberry-PWM-Object-Tracker.git
cd Raspberry-PWM-Object-Tracker

# Install Python dependencies
pip install -r requirements.txt

# Install pigpio (PWM control)
sudo apt-get install pigpio python-pigpio python3-pigpio
sudo systemctl start pigpiod
sudo systemctl enable pigpiod
```

#### 2. Download Model Files
```bash
# Download MobileNetSSD model
wget -P models/ https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/deploy.prototxt
wget -P models/ https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/mobilenet_iter_73000.caffemodel
mv models/deploy.prototxt models/MobileNetSSD_deploy.prototxt
mv models/mobilenet_iter_73000.caffemodel models/MobileNetSSD_deploy.caffemodel

# Download face detection model
wget -P models/ https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
wget -P models/ https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel
```

#### 3. Prepare Face Images
Put face images for recognition in the `img/` directory:
- `xxx.jpg`
- `xxx.jpg`
- `xxx.jpg`

## 📁 Project Structure

```
Raspberry-PWM-Object-Tracker/
├── README.md              # Project documentation (Chinese)
├── README.en.md           # Project documentation (English)
├── requirements.txt       # Python dependencies
├── docs/                  # Technical documentation
│   ├── DOCKER_SETUP.md   # Docker deployment guide
│   └── docker-usage.md   # Docker usage instructions
├── img/                   # Face recognition images
│   └── README.md         # Image instructions
└── src/                   # Source code
    ├── stranger.py       # Stranger detection main program
    ├── search_xx_rec.py  # Object detection program
    ├── search_face.py    # Face detection program
    ├── vplay.py          # Video player
    ├── myCam1.py         # Multi-threaded camera class
    ├── myCam0.py         # Basic camera class
    └── myPWM.py          # PWM control module
```

## 🚪 Usage

### 1. Stranger Detection
```bash
cd src
python stranger.py
```

### 2. Detect Specific Objects
```bash
cd src
# Detect dog
python search_xx_rec.py -o 12

# Detect cat
python search_xx_rec.py -o 8

# Detect car
python search_xx_rec.py -o 7
```

### 3. Face Detection
```bash
cd src
python search_face.py
```

### 4. Play Recorded Video
```bash
cd src
python vplay.py -v ../output/output.mp4

# Set playback speed (0.2 seconds per frame)
python vplay.py -v ../output/output.mp4 -s 20
```

## 🐳 Docker Deployment

### Quick Execution
```bash
# Detect dog
docker run -it --rm -v /dev:/dev --privileged \
  -v /etc/localtime:/etc/localtime:ro \
  -e "LANG=C.UTF-8" \
  -p 9090:9090 \
  -v $(pwd):/app \
  -w /app/src \
  cv2-ocr-lcd-gpio-fr:cv3.3 python search_xx_rec.py -o 12
```

For detailed Docker usage, please refer to [docs/DOCKER_SETUP.md](docs/DOCKER_SETUP.md).

## 🔧 Configuration

### Tracking Sensitivity
Adjust the following parameters in `stranger.py` or `search_xx_rec.py`:

```python
ADJ_DIFF = 80      # Pixel difference to trigger adjustment (default: 80)
ADJ_STEP = 1       # Angle step per adjustment (default: 1)
CONFIDENCE = 0.6   # Detection confidence threshold (default: 0.6)
SKIPFLAME = 1      # Skip frames after adjustment (default: 1)
```

### Camera Resolution
Adjust in `myCam1.py`:

```python
# Lower resolution, better performance
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Higher resolution, better quality
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```

## 📝 Usage Examples

### Example 1: Classroom Monitoring
```bash
# Monitor classroom, identify teachers and students
cd src
python stranger.py

# Open in browser
# http://raspberry-pi-ip:9090/a.mjpg
```

### Example 2: Pet Monitor
```bash
# Detect pets at home
cd src
python search_xx_rec.py -o 12  # dog
python search_xx_rec.py -o 8   # cat
```

### Example 3: Parking Lot Vehicle Detection
```bash
# Detect vehicles entering/exiting parking lot
cd src
python search_xx_rec.py -o 7   # car
```

## 🛠️ Troubleshooting

### Problem 1: Camera Not Found
```
Error: capture.isOpened(): False
Solution:
1. Check camera connection
2. Check /dev/video* permissions: sudo chmod 666 /dev/video0
3. Add user to video group: sudo usermod -a -G video $USER
```

### Problem 2: PWM Connection Failed
```
Error: Cannot connect to pigpio daemon
Solution:
1. Confirm pigpiod service is running: sudo systemctl status pigpiod
2. Check firewall settings
3. Confirm correct IP in Docker environment (default: 172.17.0.1:8888)
```

### Problem 3: Model Files Missing
```
Error: Cannot load model files
Solution:
1. Confirm models/ directory has correct files
2. Download missing model files (refer to Installation Step 2)
3. Check file permissions
```

## 📄 License

MIT License

## 🌐 Language Versions
- [Chinese Version](README.md)
- [English Version](README.en.md)

---

**Note**: Please comply with local privacy regulations when using. For academic research and educational purposes only.
