# ESP32 MicroPython 燒錄腳本
# 適用於 Type-C 接口的 ESP32 開發板

echo "=== ESP32 MicroPython 燒錄工具 ==="
echo ""

# 檢查 esptool 是否安裝
if ! command -v esptool.py &> /dev/null; then
    echo "請先安裝 esptool:"
    echo "pip install esptool"
    exit 1
fi

# 設定參數
PORT=${1:-/dev/ttyUSB0}
BAUD=460800
FIRMWARE_URL="https://micropython.org/resources/firmware/esp32-20230902-v1.21.0.bin"
FIRMWARE_FILE="esp32-micropython.bin"

echo "目標板: ESP32 (Type-C)"
echo "序列埠: $PORT"
echo ""

# 下載韌體
echo "1. 下載 MicroPython 韌體..."
if [ ! -f "$FIRMWARE_FILE" ]; then
    wget -O "$FIRMWARE_FILE" "$FIRMWARE_URL" || {
        echo "下載失敗，請手動下載:"
        echo "$FIRMWARE_URL"
        exit 1
    }
fi

echo "2. 清除快閃記憶體..."
esptool.py --chip esp32 --port "$PORT" --baud $BAUD erase_flash

echo "3. 燒錄 MicroPython..."
esptool.py --chip esp32 --port "$PORT" --baud $BAUD write_flash -z 0x1000 "$FIRMWARE_FILE"

echo ""
echo "✅ 燒錄完成！"
echo "現在可以使用 Thonny IDE 或 ampy 上傳程式碼"
