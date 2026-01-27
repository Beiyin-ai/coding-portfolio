# 使用 ampy 上傳檔案到 ESP32

echo "=== ESP32 檔案上傳工具 ==="
echo ""

# 檢查 ampy 是否安裝
if ! command -v ampy &> /dev/null; then
    echo "請先安裝 ampy:"
    echo "pip install adafruit-ampy"
    exit 1
fi

# 設定參數
PORT=${1:-/dev/ttyUSB0}
BAUD=115200
FIRMWARE_DIR="firmware"

echo "目標: $PORT"
echo "上傳目錄: $FIRMWARE_DIR"
echo ""

# 上傳檔案
echo "上傳檔案..."
for file in "$FIRMWARE_DIR"/*.py; do
    if [ -f "$file" ]; then
        echo "上傳: $(basename "$file")"
        ampy --port "$PORT" --baud $BAUD put "$file" "/$(basename "$file")"
    fi
done

# 上傳 lib 資料夾
if [ -d "$FIRMWARE_DIR/lib" ]; then
    echo "上傳 lib/ 資料夾..."
    ampy --port "$PORT" --baud $BAUD put "$FIRMWARE_DIR/lib" "/lib"
fi

echo ""
echo "✅ 上傳完成！"
echo "ESP32 將自動重啟並執行 main.py"
