# database/models.py
from database.db_connection import get_db_connection

def insert_sensor_data(data):
    """存入感測器數據"""
    conn = get_db_connection()
    if not conn:
        return None
    
    cursor = conn.cursor()
    
    try:
        insert_query = """
            INSERT INTO sensor_data (
                device_id, bus_voltage, shunt_voltage, load_voltage,
                current_ma, power_mw, temperature_c, humidity_percent,
                illuminance_raw, timestamp_esp, solar_voltage
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        insert_values = (
            data['device_id'],
            data.get('bus_voltage'),
            data.get('shunt_voltage'),
            data.get('load_voltage'),
            data.get('current_ma'),
            data.get('power_mw'),
            data.get('temperature_c'),
            data.get('humidity_percent'),
            data.get('illuminance_raw'),
            data.get('timestamp_esp'),
            data.get('solar_voltage', 0)
        )
        
        cursor.execute(insert_query, insert_values)
        conn.commit()
        
        record_id = cursor.lastrowid
        return record_id
        
    except Exception as e:
        print(f"❌ 插入資料錯誤: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_latest_data(limit=10):
    """取得最新數據"""
    conn = get_db_connection()
    if not conn:
        return None
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT * FROM sensor_data 
            ORDER BY created_at DESC 
            LIMIT %s
        """, (limit,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def get_history_data(hours=24, device='%', limit=100):
    """取得歷史數據"""
    conn = get_db_connection()
    if not conn:
        return None
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
            SELECT * FROM sensor_data 
            WHERE device_id LIKE %s 
            AND created_at >= NOW() - INTERVAL %s HOUR
            ORDER BY created_at DESC
            LIMIT %s
        """
        cursor.execute(query, (device, hours, limit))
        return cursor.fetchall()
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