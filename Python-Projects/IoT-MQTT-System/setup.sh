
echo "🔧 IoT-MQTT 系統安裝腳本"
echo "======================="
echo "課程：物聯網通訊實務 - 謝燿聰老師"
echo ""

# 檢查必要工具
echo "1. 檢查系統環境..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安裝"
    exit 1
fi
echo "   ✅ Python3: $(python3 --version)"

if ! command -v pip &> /dev/null; then
    echo "⚠️  pip 未安裝，嘗試安裝..."
    sudo apt update && sudo apt install python3-pip -y
fi
echo "   ✅ pip: $(pip --version)"

# 安裝 Python 套件
echo ""
echo "2. 安裝 Python 套件..."
pip install -r requirements.txt

# 建立日誌目錄
echo ""
echo "3. 建立日誌目錄..."
mkdir -p ~/log_mqtt
echo "   日誌目錄: ~/log_mqtt"

# 顯示完成訊息
echo ""
echo "✅ 安裝完成！"
echo ""
echo "📋 使用方法："
echo "1. 啟動 MQTT Broker:"
echo "   docker run -d -p 1883:1883 --name mqtt_broker eclipse-mosquitto"
echo ""
echo "2. 執行訂閱者:"
echo "   python subscriber.py"
echo ""
echo "3. 執行發布者:"
echo "   python publisher.py"
echo ""
echo "🔍 詳細說明請參閱 run-instructions.txt"


echo "🔧 IoT-MQTT 系統安裝腳本"
echo "======================="
echo "課程：物聯網通訊實務 - 謝燿聰老師"
echo "學生：邱佩吟"
echo ""

# 檢查必要工具
echo "1. 檢查系統環境..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安裝"
    exit 1
fi
echo "   ✅ Python3: $(python3 --version)"

if ! command -v pip &> /dev/null; then
    echo "⚠️  pip 未安裝，嘗試安裝..."
    sudo apt update && sudo apt install python3-pip -y
fi
echo "   ✅ pip: $(pip --version)"

# 安裝 Python 套件
echo ""
echo "2. 安裝 Python 套件..."
pip install -r requirements.txt

# 建立日誌目錄
echo ""
echo "3. 建立日誌目錄..."
mkdir -p ~/log_mqtt
echo "   日誌目錄: ~/log_mqtt"

# 顯示完成訊息
echo ""
echo "✅ 安裝完成！"
echo ""
echo "📋 使用方法："
echo "1. 啟動 MQTT Broker:"
echo "   docker run -d -p 1883:1883 --name mqtt_broker eclipse-mosquitto"
echo ""
echo "2. 執行訂閱者:"
echo "   python subscriber.py"
echo ""
echo "3. 執行發布者:"
echo "   python publisher.py"
echo ""
echo "🔍 詳細說明請參閱 run-instructions.txt"
