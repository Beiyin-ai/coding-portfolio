# ESP32 Smart Desktop Display / ESP32 智能桌面顯示器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: ESP32](https://img.shields.io/badge/Platform-ESP32-green.svg)](https://www.espressif.com/)
[![Framework: Arduino](https://img.shields.io/badge/Framework-Arduino-blue.svg)](https://www.arduino.cc/)

## 📋 專案概述 / Project Overview

這是一個物聯網學習專案，整合多種感測器和顯示技術，建立一個智能桌面顯示裝置。專案作為 ESP32 開發、感測器整合和使用者介面設計的練習。

This is a practice IoT project that integrates multiple sensors and display technologies to create a smart desktop display device. The project serves as a learning exercise for ESP32 development, sensor integration, and user interface design.

## 🎯 學習目標 / Learning Objectives
- **ESP32 微控制器程式設計** / ESP32 microcontroller programming
- **多感測器整合** / Multiple sensor integration (DHT22, OLED, WS2812B)
- **OLED 顯示介面設計** / User interface design with OLED display
- **按鈕互動與狀態管理** / Button interaction and state management
- **物聯網系統架構** / IoT system architecture

## 📸 專案展示 / Project Demo

*(請在 docs/images/ 資料夾中放置展示圖片或 GIF)*
*(Please place demo images or GIFs in docs/images/ folder)*

## 🛠 硬體元件 / Hardware Components
| 元件 / Component | 規格 / Specification | 數量 / Qty |
|-----------------|---------------------|------------|
| ESP32 開發板 | ESP32-WROOM-32 | 1 |
| OLED 顯示器 | 0.96" I2C SSD1306 | 1 |
| 溫濕度感測器 | DHT22 | 1 |
| RGB LED | WS2812B | 1 |
| 按鈕開關 | 輕觸開關 | 1 |
| 麵包板與杜邦線 | Breadboard & jumper wires | 1套 |

## 🔌 電路接線 / Wiring Diagram
詳細接線說明請見：[接線指南](docs/wiring_guide.md) / See [Wiring Guide](docs/wiring_guide.md) for detailed connection instructions.

基本接線 / Basic Wiring:
ESP32 3.3V → OLED VCC, DHT22 VCC, WS2812B VDD
ESP32 GND → OLED GND, DHT22 GND, WS2812B VSS, Button
ESP32 GPIO21 → OLED SDA
ESP32 GPIO22 → OLED SCL
ESP32 GPIO4 → DHT22 DATA
ESP32 GPIO13 → WS2812B DIN
ESP32 GPIO15 → Button (內部上拉電阻 / with internal pull-up)

## 💻 軟體功能 / Software Features

### 四種顯示模式 / Four Display Modes
1. **正常模式 / Normal Mode**：顯示日期、時間、溫濕度
2. **倒數模式 / Counter Mode**：大字顯示目標倒數
3. **訊息模式 / Message Mode**：輪播預設文字訊息
4. **特別模式 / Special Mode**：動畫顯示與彩虹LED效果

### 互動控制 / Interactive Controls
- **短按按鈕 / Short press**：循環切換顯示模式
- **長按2秒 / Long press (2s)**：觸發特別動畫
- **自動輪播 / Automatic rotation**：訊息自動定時更換

## 🚀 快速開始 / Getting Started

### 環境需求 / Prerequisites
- PlatformIO 或 Arduino IDE
- ESP32 開發板支援
- 必要函式庫 / Required libraries:
  ```bash
  # PlatformIO 會自動安裝 / PlatformIO will install automatically
  - U8g2 (OLED顯示)
  - DHT sensor library (溫濕度感測)
  - FastLED (RGB LED控制)
安裝步驟 / Installation Steps
# 複製專案 / Clone the project
git clone <repository-url>
cd ESP32-Smart-Desktop-Display

# 編譯與上傳 / Build and upload
cd firmware
pio run --target upload

# 監控序列埠 / Monitor serial output
pio device monitor
設定檔修改 / Configuration
編輯 firmware/src/config.h 可客製化：

顯示訊息內容 / Display messages

LED 顏色設定 / LED colors

更新時間間隔 / Update intervals

目標日期設定 / Target date settings

📂 專案結構 / Project Structure
ESP32-Smart-Desktop-Display/
├── firmware/           # 韌體程式碼
│   ├── src/           # 原始碼
│   └── platformio.ini # PlatformIO 設定
├── docs/              # 文件
│   ├── wiring_guide.md
│   └── setup_guide.md
├── hardware/          # 硬體設計
│   ├── BOM.md
│   └── schematic/
├── examples/          # 範例程式
└── simulations/       # 模擬測試
📝 程式碼範例 / Code Example
// 設定檔範例 / Configuration example
#define OLED_SDA_PIN 21
#define OLED_SCL_PIN 22
#define DHT_PIN 4
#define LED_PIN 13
#define BUTTON_PIN 15

const char* MARQUEE_MESSAGES[] = {
  "Birthday in 9 days",
  "IoT Learning Project",
  "ESP32 + OLED + DHT22",
  "Smart Desktop Display"
};
🤝 貢獻指南 / Contributing
歡迎提交 Issue 或 Pull Request！
Contributions are welcome! Please feel free to submit a Pull Request.

📄 授權條款 / License
本專案採用 MIT 授權 - 詳見 LICENSE 檔案
This project is licensed under the MIT License - see the LICENSE file for details.

📧 聯絡資訊 / Contact
GitHub: @Beiyin-ai

專案連結: ESP32-Smart-Desktop-Display

## 🔧 安裝與設定
# Setup Guide

## Prerequisites
- Arduino IDE or PlatformIO
- ESP32 Board Support
- Required Libraries:
  - U8g2 (for OLED)
  - DHT sensor library
  - FastLED

## Installation Steps

### 1. Install PlatformIO
```bash
# Install PlatformIO Core
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/platformio/platformio/master/scripts/get-platformio.py)"
2. Clone the Project
bash
git clone <repository-url>
cd ESP32-Smart-Desktop-Display
3. Build and Upload
bash
cd firmware
pio run --target upload
4. Monitor Serial Output
bash
pio device monitor
Configuration
Edit firmware/src/config.h to customize:

Display messages

LED colors

Update intervals

Animation parameters

## 💻 使用範例
# 基本使用範例

這個範例展示如何初始化和使用 ESP32 智能桌面顯示器的主要功能。

## 初始化程式碼

```cpp
#include <Arduino.h>
#include "config.h"
#include "led.h"
#include "button.h"

LED ledControl;
Button button;

void setup() {
  Serial.begin(115200);
  ledControl.init();
  button.init();
  
  Serial.println("System initialized");
}

void loop() {
  button.update();
  
  if (button.wasPressed()) {
    if (button.isLongPress()) {
      Serial.println("Long press detected!");
      ledControl.playAnimation();
    } else {
      Serial.println("Short press detected!");
      ledControl.setColor(255, 0, 0); // Red
    }
  }
  
  delay(10);
}
```
