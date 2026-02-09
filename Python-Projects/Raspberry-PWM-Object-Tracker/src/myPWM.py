# myPWM.py
# 使用 pigpio 庫控制 PWM 信號，通常用於控制伺服馬達
# 此程式透過網路連接遠端 Raspberry Pi 的 pigpio 服務

import pigpio  # 用於控制 Raspberry Pi GPIO 的庫
import time    # 用於時間控制

# 常數定義
PWM_CONTROL_PIN = 18  # 控制 PWM 輸出的 GPIO 針腳編號 (BCM編號)
PWM_FREQ = 50         # PWM 頻率 (Hz)，常用於伺服馬達控制

# 連接遠端 Raspberry Pi 的 pigpio 服務
# 參數1: 遠端主機 IP 地址
# 參數2: pigpio 服務連接埠 (預設為 8888)
pi = pigpio.pi('172.17.0.1', 8888)


def r_h(angle=90, sleepSec=0.16, oldAngle=-1, frame_x_center=-1, face_x_center=-1):
    """
    控制伺服馬達旋轉到指定角度
    
    參數:
        angle (int): 目標角度 (0-180度，預設90度)
        sleepSec (float): 執行後暫停時間 (秒)
        oldAngle (int): 之前的旋轉角度，用於紀錄
        frame_x_center (int): 畫面中心座標，用於視覺追蹤
        face_x_center (int): 人臉中心座標，用於視覺追蹤
    
    回傳值:
        int: 設定的角度值
    """
    # 計算對應角度的 PWM 脈衝寬度
    # 公式: 500Hz + (1900Hz * angle / 180)
    # 此計算方式將角度轉換為伺服馬達的控制脈衝
    duty_cycle = int(500 * PWM_FREQ + (1900 * PWM_FREQ * angle / 180))
    
    # 硬體 PWM 輸出
    # 參數1: GPIO 針腳
    # 參數2: PWM 頻率
    # 參數3: PWM 工作週期 (佔空比)
    pi.hardware_PWM(PWM_CONTROL_PIN, PWM_FREQ, duty_cycle)
    
    # 等待伺服馬達移動到指定位置
    # 若 sleepSec 參數不在合理範圍 (0-0.5秒)，則使用預設值 0.32秒
    time.sleep(sleepSec if 0 < sleepSec < 0.5 else 0.32)
    
    # 輸出旋轉資訊
    print('原角度={: >3}, 新角度={: >3}, sleep={:.2f}, frame_x_center={: >3}, faceX_center={: >3}'.format(
        oldAngle, angle, sleepSec, frame_x_center, face_x_center))
    
    return angle


def mm_close():
    """
    程式結束時執行，目前僅輸出結束訊息
    可擴展用於清理資源或關閉連線
    """
    print(f"{__name__}.py : mm_close() 結束")
    # 注意: 此函數目前未關閉 pigpio 連線，可能需要擴展功能
