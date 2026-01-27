# boot.py - 開機設定檔案
import network
import ntptime
import time
from machine import RTC

def connect_wifi(ssid, password):
    """連接 WiFi"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('連接 WiFi...')
        wlan.connect(ssid, password)

        # 等待連接，最多 10 秒
        for _ in range(20):
            if wlan.isconnected():
                break
            time.sleep(0.5)

    if wlan.isconnected():
        print('WiFi 已連接:', wlan.ifconfig())
        return True
    else:
        print('WiFi 連接失敗')
        return False

def sync_ntp():
    """同步網路時間"""
    try:
        # 設置時區 (台灣 UTC+8)
        ntptime.host = "pool.ntp.org"
        ntptime.settime()

        # 調整時區
        rtc = RTC()
        tm = time.localtime()
        tm_adj = (tm[0], tm[1], tm[2], tm[3] + 8, tm[4], tm[5], tm[6], tm[7])
        rtc.datetime(tm_adj)

        print("時間已同步:", time.localtime())
        return True
    except Exception as e:
        print("NTP 同步失敗:", e)
        return False

# 主要設定
SSID = "Beiyin"
PASSWORD = "macarena67"

# 嘗試連接 WiFi
if connect_wifi(SSID, PASSWORD):
    # 同步時間
    sync_ntp()
else:
    print('使用本機時間')

print("系統啟動完成")
