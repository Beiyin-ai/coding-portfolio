# config.py
# 所有設定集中在這裡

# MySQL 資料庫設定
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',  # 你設定的密碼
    'database': 'energy_monitor',
    'charset': 'utf8mb4'
}

# 伺服器設定
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000
DEBUG_MODE = True