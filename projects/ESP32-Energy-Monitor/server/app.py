from flask import Flask, request, jsonify
from datetime import datetime
import mysql.connector
from mysql.connector import Error
import json

app = Flask(__name__)

# ===== MySQL 資料庫連線設定 =====
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',           # 我們剛剛建立的使用者
    'password': '',  # 你設定的密碼
    'database': 'energy_monitor',
    'charset': 'utf8mb4'
}

def get_db_connection():
    """建立 MySQL 連線"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"❌ 資料庫連線錯誤: {e}")
        return None

def init_database():
    """初始化資料庫（建立表格如果不存在）"""
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            # 檢查表格是否存在，如果不存在就建立
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sensor_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    device_id VARCHAR(50) NOT NULL,
                    bus_voltage FLOAT,
                    shunt_voltage FLOAT,
                    load_voltage FLOAT,
                    current_ma FLOAT,
                    power_mw FLOAT,
                    temperature_c FLOAT,
                    humidity_percent FLOAT,
                    illuminance_raw INT,
                    timestamp_esp INT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # 建立索引（如果不存在）
            cursor.execute("SHOW INDEX FROM sensor_data WHERE Key_name = 'idx_created_at'")
            if not cursor.fetchone():
                cursor.execute("CREATE INDEX idx_created_at ON sensor_data(created_at)")
                print("✅ 建立 created_at 索引")
            
            cursor.execute("SHOW INDEX FROM sensor_data WHERE Key_name = 'idx_device_id'")
            if not cursor.fetchone():
                cursor.execute("CREATE INDEX idx_device_id ON sensor_data(device_id)")
                print("✅ 建立 device_id 索引")
            
            conn.commit()
            print("✅ 資料表初始化完成")
            
        except Error as e:
            print(f"❌ 初始化資料庫錯誤: {e}")
        finally:
            cursor.close()
            conn.close()

# 啟動時初始化資料庫
init_database()

@app.route('/')
def home():
    """首頁：顯示 API 狀態"""
    return jsonify({
        "status": "running",
        "message": "能源監控系統 API 運行中",
        "endpoints": {
            "POST /api/sensor-data": "接收感測器數據",
            "GET /api/latest": "取得最新數據",
            "GET /api/history": "查詢歷史數據"
        }
    })

@app.route('/api/sensor-data', methods=['POST'])
def receive_sensor_data():
    """
    接收 ESP32 傳來的感測器數據
    """
    # 1. 檢查是否有 JSON 數據
    if not request.is_json:
        return jsonify({"error": "請傳送 JSON 格式的數據"}), 400
    
    try:
        # 2. 取得 JSON 數據
        data = request.get_json()
        print(f"\n📥 收到來自 {data.get('device_id', 'unknown')} 的數據")
        
        # 3. 解析數據
        device_id = data.get('device_id', 'ESP32_01')
        timestamp_esp = data.get('timestamp_esp', 0)
        
        # 電力數據
        power = data.get('power', {})
        bus_voltage = power.get('bus_voltage')
        shunt_voltage = power.get('shunt_voltage')
        load_voltage = power.get('load_voltage')
        current_ma = power.get('current_ma')
        power_mw = power.get('power_mw')
        
        # 環境數據
        env = data.get('environment', {})
        temperature_c = env.get('temperature_c')
        humidity_percent = env.get('humidity_percent')
        illuminance_raw = env.get('illuminance_raw')
        # 太陽能板數據（新增！）
        solar_voltage = data.get('solar_voltage', 0)
        
        # 4. 存入 MySQL
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "資料庫連線失敗"}), 500
        
        cursor = conn.cursor()
        
        insert_query = """
            INSERT INTO sensor_data (
                device_id, bus_voltage, shunt_voltage, load_voltage,
                current_ma, power_mw, temperature_c, humidity_percent,
                illuminance_raw, timestamp_esp,
                solar_voltage
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        insert_values = (
            device_id, bus_voltage, shunt_voltage, load_voltage,
            current_ma, power_mw, temperature_c, humidity_percent,
            illuminance_raw, timestamp_esp,
            solar_voltage
        )
        
        cursor.execute(insert_query, insert_values)
        conn.commit()
        
        # 5. 顯示成功訊息
        print(f"✅ 數據已存入資料庫 (ID: {cursor.lastrowid})")
        print(f"   功率: {power_mw} mW, 溫度: {temperature_c}°C, 濕度: {humidity_percent}%")
        
        cursor.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "message": "數據已存入資料庫",
            "record_id": cursor.lastrowid,
            "received_at": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        print(f"❌ 處理數據時發生錯誤: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/latest', methods=['GET'])
def get_latest_data():
    """
    取得最新的感測器數據
    """
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "資料庫連線失敗"}), 500
        
        cursor = conn.cursor(dictionary=True)
        
        # 取得最新 10 筆數據
        cursor.execute("""
            SELECT * FROM sensor_data 
            ORDER BY created_at DESC 
            LIMIT 10
        """)
        
        results = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "count": len(results),
            "data": results
        }), 200
        
    except Exception as e:
        print(f"❌ 查詢數據時發生錯誤: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """
    查詢歷史數據（可依時間範圍）
    使用方式: /api/history?hours=24&device=ESP32_01
    """
    try:
        # 取得查詢參數
        hours = request.args.get('hours', default=24, type=int)
        device = request.args.get('device', default='%', type=str)
        limit = request.args.get('limit', default=100, type=int)
        
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "資料庫連線失敗"}), 500
        
        cursor = conn.cursor(dictionary=True)
        
        # 查詢指定時間範圍的數據
        query = """
            SELECT * FROM sensor_data 
            WHERE device_id LIKE %s 
            AND created_at >= NOW() - INTERVAL %s HOUR
            ORDER BY created_at DESC
            LIMIT %s
        """
        
        cursor.execute(query, (device, hours, limit))
        results = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "query": {
                "hours": hours,
                "device": device,
                "limit": limit
            },
            "count": len(results),
            "data": results
        }), 200
        
    except Exception as e:
        print(f"❌ 查詢數據時發生錯誤: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 能源監控系統伺服器啟動中...")
    print(f"📅 啟動時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # 測試資料庫連線
    conn = get_db_connection()
    if conn:
        print("✅ MySQL 資料庫連線成功")
        conn.close()
    else:
        print("❌ MySQL 資料庫連線失敗，請檢查設定")
    
    print("\n📡 等待 ESP32 傳送數據...")
    print("=" * 50)
    
    # 啟動 Flask 伺服器
    app.run(host='0.0.0.0', port=5000, debug=True)