# IoT MQTT Messaging System

A complete Dockerized MQTT subscriber system implementation project, based on Professor Xie Yaocong's IoT Communication Practice course materials.

## 🎯 Project Features

✅ **Complete Implementation** - Includes complete MQTT subscriber and publisher implementation
✅ **Containerized Deployment** - Uses Docker containerization technology for easy deployment
✅ **Practical Testing** - Actually tested and verified in Ubuntu environment
✅ **Complete Documentation** - Includes detailed execution instructions and architecture documents
✅ **Education Oriented** - Based on course materials, suitable for learning reference

## 📁 Project Structure

```
IoT-MQTT-System/
├── README.md                 # Chinese documentation
├── README.en.md              # English documentation
├── .gitignore                # Git ignore settings
├── requirements.txt          # Python package list
├── Dockerfile                # Docker build file
├── appRun.sh                 # Container startup script
├── subscriber.py             # Basic subscriber program
├── tmp-sub.py                # Advanced subscriber program
├── publisher.py              # Publisher program
├── run-instructions.txt      # Complete execution instructions
├── setup.sh                  # One-click installation script
└── docs/                     # Documentation directory
    └── ARCHITECTURE.md       # System architecture description
```

## 🚀 Quick Start

### Method 1: Easiest way (using setup.sh)
```bash
# Give execution permission
chmod +x setup.sh

# Run installation script
./setup.sh
```

### Method 2: Manual installation
```bash
# 1. Install Python packages
pip install -r requirements.txt

# 2. Start MQTT Broker
docker run -d -p 1883:1883 --name mqtt_broker eclipse-mosquitto

# 3. Run subscriber
python subscriber.py

# 4. Publish test message (in another terminal)
python publisher.py
```

### Method 3: Using Docker containerized execution
```bash
# 1. Build Docker image
docker build -t iot_mqtt:112 .

# 2. Run container
docker run -d \
    --name iot_mqtt \
    --restart unless-stopped \
    -v $(pwd):/x \
    -v ~/log_mqtt:/xlog_mqtt \
    iot_mqtt:112
```

## 📚 Learning Points

1. **MQTT Communication Protocol**: Understanding publish/subscribe model
2. **Python MQTT Programming**: Using paho-mqtt package
3. **Docker Containerization**: Application containerization deployment
4. **System Integration**: MQTT + HTTP data transmission
5. **Practical Operation**: Terminal commands and Python program testing

## 👩‍💻 Author

**Qiu Peiyin (邱佩吟)**
- Course: IoT Communication Practice
- Professor: Xie Yaocong
- Completion Date: January 2026

## 📄 License

This project is for learning reference only, adapted from course materials.
