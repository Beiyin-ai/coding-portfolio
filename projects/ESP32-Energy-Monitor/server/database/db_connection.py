# database/db_connection.py
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

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
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        
        # 建立表格（修正：加上 solar_voltage 欄位）
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
                solar_voltage FLOAT,
                timestamp_esp INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # 建立索引
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

def test_connection():
    """測試資料庫連線"""
    conn = get_db_connection()
    if conn:
        conn.close()
        return True
    return False