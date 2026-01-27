# MicroPython 開發環境設定指南

## 📋 系統需求
- Windows / macOS / Linux
- Python 3.7 或更高版本
- USB Type-C 數據線
- 網路連接

## 🚀 快速開始

### 1. 安裝必要工具
```bash
# 安裝 Python 套件
pip install esptool adafruit-ampy

# 檢查安裝
esptool.py version
ampy --help
```

### 2. 燒錄 MicroPython 韌體
```bash
# 使用提供的腳本
cd tools
./flash_micropython.sh /dev/ttyUSB0

# 或手動燒錄
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 \
  erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 \
  write_flash -z 0x1000 esp32-micropython.bin
```

### 3. 上傳專案檔案
```bash
# 使用腳本
cd tools
./upload_files.sh /dev/ttyUSB0

# 或手動上傳
ampy --port /dev/ttyUSB0 put ../firmware/main.py
ampy --port /dev/ttyUSB0 put ../firmware/boot.py
```

## 🛠️ 使用 Thonny IDE (推薦)

### 安裝 Thonny
1. 下載: https://thonny.org
2. 安裝並開啟

### 設定 Thonny
1. **工具** → **選項** → **直譯器**
2. 選擇: **MicroPython (ESP32)**
3. 選擇正確的序列埠
4. 點擊 **安裝/更新 MicroPython 韌體**

### 上傳檔案
1. 開啟 `firmware/main.py`
2. **檔案** → **另存為** → **MicroPython 裝置**
3. 輸入檔名: `main.py`
4. 重複步驟上傳 `boot.py`

## 🔧 序列埠監控

### 在 Thonny 中
- 下方視窗即是序列埠監控
- 可看到程式輸出和錯誤訊息

### 使用 ampy
```bash
# 查看序列輸出
ampy --port /dev/ttyUSB0 run -n firmware/main.py

# 進入 REPL 模式
ampy --port /dev/ttyUSB0 terminal
```
