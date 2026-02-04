# Raspberry Pi Face Recognition and Object Tracking System

A smart camera system based on Raspberry Pi, OpenCV, and PWM control, featuring face recognition, object detection, and auto-tracking capabilities.

## 🎯 Features
- **Multi-face Recognition**: Identify known persons and mark strangers
- **Object Detection**: Supports 20 MobileNetSSD object categories
- **Auto-tracking**: Automatically adjusts camera angle based on detected targets
- **Real-time Streaming**: HTTP streaming server for remote viewing
- **PWM Control**: Precise servo motor angle control
- **Docker Support**: Containerized deployment for easy portability

## 📊 Supported Object Classes
\`\`\`python
# 20 MobileNetSSD supported classes:
1: aeroplane, 2: bicycle, 3: bird, 4: boat, 5: bottle
6: bus, 7: car, 8: cat, 9: chair, 10: cow
11: diningtable, 12: dog, 13: horse, 14: motorbike
15: person, 16: pottedplant, 17: sheep, 18: sofa
19: train, 20: tvmonitor
\`\`\`

## 🚀 Quick Start

### Hardware Requirements
- Raspberry Pi
- USB Camera
- SG90 Servo Motor
- PCA9685 PWM Expansion Board (Optional)

### Software Requirements
- Python 3.7+
- OpenCV 4.5+
- Docker (Optional)

### Installation Steps

\`\`\`bash
# 1. Clone the project
git clone <your-repo-url>
cd Raspberry-PWM-Object-Tracker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install pigpio
sudo apt-get install pigpio python-pigpio python3-pigpio

# 4. Start pigpio daemon
sudo systemctl start pigpiod
\`\`\`
