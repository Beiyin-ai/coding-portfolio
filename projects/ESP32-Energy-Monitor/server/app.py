# app.py
from flask import Flask
from api.routes import api_bp
from database.db_connection import init_database, test_connection
from config import SERVER_HOST, SERVER_PORT, DEBUG_MODE
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 能源監控系統伺服器啟動中（模組化版本）...")
    print(f"📅 啟動時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔌 監聽埠口: {SERVER_PORT}")
    print("=" * 50)
    
    init_database()
    
    if test_connection():
        print("✅ MySQL 資料庫連線成功")
    else:
        print("❌ MySQL 資料庫連線失敗，請檢查設定")
    
    print("\n📡 等待 ESP32 傳送數據...")
    print("=" * 50)
    
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=DEBUG_MODE)