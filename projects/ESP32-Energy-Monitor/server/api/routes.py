# api/routes.py
from flask import Blueprint, request, jsonify
from datetime import datetime
from database import models

# 建立 Blueprint
api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
    """首頁：顯示 API 狀態"""
    return jsonify({
        "status": "running",
        "message": "能源監控系統 API 運行中（模組化版本）",
        "port": 5001,
        "endpoints": {
            "POST /api/sensor-data": "接收感測器數據",
            "GET /api/latest": "取得最新數據",
            "GET /api/history": "查詢歷史數據"
        }
    })

@api_bp.route('/sensor-data', methods=['POST'])
def receive_sensor_data():
    """接收 ESP32 傳來的感測器數據"""
    
    if not request.is_json:
        return jsonify({"error": "請傳送 JSON 格式的數據"}), 400
    
    try:
        data = request.get_json()
        print(f"\n📥 收到來自 {data.get('device_id', 'unknown')} 的數據")
        
        device_id = data.get('device_id', 'ESP32_01')
        timestamp_esp = data.get('timestamp_esp', 0)
        
        power = data.get('power') or {}
        env = data.get('environment') or {}
        
        bus_voltage = power.get('bus_voltage')
        shunt_voltage = power.get('shunt_voltage')
        load_voltage = power.get('load_voltage')
        current_ma = power.get('current_ma')
        power_mw = power.get('power_mw')
        
        temperature_c = env.get('temperature_c')
        humidity_percent = env.get('humidity_percent')
        illuminance_raw = env.get('illuminance_raw')
        solar_voltage = data.get('solar_voltage', 0)
        
        if power_mw is None:
            return jsonify({"error": "power_mw missing"}), 400
        
        sensor_data = {
            'device_id': device_id,
            'timestamp_esp': timestamp_esp,
            'bus_voltage': bus_voltage,
            'shunt_voltage': shunt_voltage,
            'load_voltage': load_voltage,
            'current_ma': current_ma,
            'power_mw': power_mw,
            'temperature_c': temperature_c,
            'humidity_percent': humidity_percent,
            'illuminance_raw': illuminance_raw,
            'solar_voltage': solar_voltage
        }
        
        record_id = models.insert_sensor_data(sensor_data)
        
        if record_id:
            print(f"✅ 數據已存入資料庫 (ID: {record_id})")
            print(f"   功率: {power_mw} mW, 溫度: {temperature_c}°C, 濕度: {humidity_percent}%")
            
            return jsonify({
                "status": "success",
                "message": "數據已存入資料庫",
                "record_id": record_id,
                "received_at": datetime.now().isoformat()
            }), 200
        else:
            return jsonify({"error": "資料庫寫入失敗"}), 500
        
    except Exception as e:
        print(f"❌ 處理數據時發生錯誤: {e}")
        return jsonify({"error": str(e)}), 500

@api_bp.route('/latest', methods=['GET'])
def get_latest_data():
    """取得最新的感測器數據"""
    try:
        results = models.get_latest_data(limit=10)
        
        return jsonify({
            "status": "success",
            "count": len(results) if results else 0,
            "data": results if results else []
        }), 200
        
    except Exception as e:
        print(f"❌ 查詢數據時發生錯誤: {e}")
        return jsonify({"error": str(e)}), 500

@api_bp.route('/history', methods=['GET'])
def get_history():
    """查詢歷史數據"""
    try:
        hours = request.args.get('hours', default=24, type=int)
        device = request.args.get('device', default='%', type=str)
        limit = request.args.get('limit', default=100, type=int)
        
        limit = min(limit, 500)
        
        results = models.get_history_data(hours, device, limit)
        
        return jsonify({
            "status": "success",
            "query": {
                "hours": hours,
                "device": device,
                "limit": limit
            },
            "count": len(results) if results else 0,
            "data": results if results else []
        }), 200
        
    except Exception as e:
        print(f"❌ 查詢數據時發生錯誤: {e}")
        return jsonify({"error": str(e)}), 500