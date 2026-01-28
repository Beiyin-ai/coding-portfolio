# Hand Gesture ESP32 Light Control System

An intelligent interactive system using MediaPipe hand recognition technology to control ESP32 RGB LED strips via Jetson Nano.

## 🎯 Features
- **Real-time Gesture Recognition**: Accurate rock-paper-scissors recognition using MediaPipe
- **Hardware Integration Control**: Control ESP32 RGB LED strips via serial communication
- **Real-time Visual Feedback**: Display recognition results and light status
- **Cross-platform Compatibility**: Supports Jetson Nano, Raspberry Pi, and general PCs
- **Complete Error Handling**: Auto fallback to test mode on serial port failure

## 🤖 Gesture to Light Mapping
| Gesture | Code | LED Color | Description |
|---------|------|-----------|-------------|
| ✋ Paper | 1 | White (#ffffff) | All fingers open |
| ✊ Rock | 2 | Green (#33ff33) | Fist |
| ✌️ Scissors | 3 | Red (#ff0000) | Index and middle fingers open |
| ❓ Unknown/No Hand | 4 | Black/Off (#000000) | Other gestures or no hand |

## 🚀 Quick Start

### Hardware Requirements
- Jetson Nano or general PC
- ESP32 Wrover Module
- WS2812 RGB LED Strip (8 LEDs)
- USB Web Camera
- USB to TTL Serial Cable (CH340/CH341)
- Dupont cables

### Installation Steps

1. **Clone Project and Set Permissions**
```bash
cd Hand-Gesture-ESP32-Light-Control
chmod +x setup.sh run.sh
```

2. **Install Python Dependencies**
```bash
./setup.sh
# or manually install
# pip install -r requirements.txt
```

3. **Set Serial Port Permissions**
```bash
# Add user to serial port access group
sudo usermod -a -G dialout $USER
# Logout and login again for changes to take effect
# or run: newgrp dialout
```

### Upload ESP32 Firmware
1. Open `esp32/firmware.ino` in Arduino IDE
2. Install ESP32 board support
3. Install Adafruit NeoPixel library
4. Select board: ESP32 Wrover Module
5. Upload firmware to ESP32

### Usage

#### Method 1: Using Execution Script
```bash
./run.sh
```

#### Method 2: Manual Execution
```bash
cd jetson
python3 main.py
```

## 📁 Project Structure
```
Hand-Gesture-ESP32-Light-Control/
├── README.md                    # Chinese documentation
├── README.en.md                 # English documentation
├── requirements.txt             # Python dependencies
├── setup.sh                     # Installation script
├── run.sh                       # Execution script
├── jetson/                      # Jetson Nano programs
│   ├── main.py                  # Main program - gesture recognition
│   └── utils.py                 # Utility functions
├── esp32/                       # ESP32 firmware
│   ├── firmware.ino             # Arduino program - LED control
│   └── README.md                # ESP32 hardware instructions
├── docs/                        # Detailed documents
│   ├── SETUP_GUIDE.md           # Complete setup guide
│   ├── SERIAL_SETUP.md          # Serial port setup details
│   └── TROUBLESHOOTING.md       # Troubleshooting guide
└── tests/                       # Test programs
    ├── test_serial.py           # Serial communication test
    └── test_hardware.py         # Hardware connection test
```

## 🧪 Testing and Debugging

### Hardware Connection Test
```bash
cd tests
python3 test_hardware.py
```

### Serial Communication Test
```bash
cd tests
python3 test_serial.py
```

## 🛠️ Technologies Used
- **MediaPipe**: Google's hand recognition framework
- **OpenCV**: Computer vision and image processing
- **PySerial**: Serial port communication control
- **Adafruit NeoPixel**: WS2812 LED control library
- **Arduino Framework**: ESP32 embedded development

## 🎯 Learning Objectives
This project demonstrates:
1. **Computer Vision Application**: MediaPipe hand recognition implementation
2. **Embedded System Integration**: Communication between Jetson Nano and ESP32
3. **Serial Communication Protocol**: UART serial data transmission
4. **Hardware Control Programming**: WS2812 LED strip control
5. **Cross-platform Development**: Python + Arduino dual-platform collaboration

## 🔄 Future Enhancements
1. **Add More Gestures**: Recognize additional gesture commands
2. **Machine Learning Integration**: Train custom gesture classification models
3. **Network Communication**: Remote light control via WiFi
4. **Multi-device Synchronization**: Control multiple ESP32 LED strips
5. **Web Interface**: Create web monitoring and control interface

## ⚠️ Important Notes
- Ensure USB to TTL cable is correctly connected (TX↔RX crossover)
- WS2812 LED requires sufficient 5V power supply
- Serial communication requires correct baud rate (9600)
- Gesture recognition is affected by lighting and background
- First-time use requires serial port permission setup

## 📝 License
MIT License

---

## 🌐 Language Versions
- [中文版本](README.md)
- [English Version](README.en.md)
