"""
ESP32 MQTT 智慧家庭控制器 - 主程式
功能：訂閱 MQTT 主題，控制繼電器、伺服馬達、LCD 顯示器
"""

from machine import Pin, I2C, PWM
import time, network, ntptime
from umqtt.robust import MQTTClient
from machine_i2c_lcd import I2cLcd

# ========== 使用者需修改的設定 ==========
WiFi_ssid = "你的WiFi名稱"           # 修改為你的 WiFi SSID
WiFi_password = "你的WiFi密碼"       # 修改為你的 WiFi 密碼

mqtt_broker = '你的MQTT Broker IP'   # 修改為你的 MQTT Broker 位址
mqtt_port   = 443                    # MQTT 埠號

mqtt_client_id = 'esp32-client-01'   # 可自訂客戶端 ID
topic_head  = b'your/topic/prefix'   # 修改為你的主題前綴
# =====================================

# MQTT 主題設定
topic_all   = topic_head + b'/#'
topic_servo = topic_head + b'/servo'
topic_lcd   = topic_head + b'/LCD'
topic_relay = topic_head + b'/relay'

# NTP 時間伺服器（台灣）
ntptime.host='tw.pool.ntp.org' 

# ========== 硬體腳位設定 ==========
GPIO_relay = Pin(13, Pin.OUT)        # 繼電器控制腳位（低電位觸發）
GPIO_led = Pin(2, Pin.OUT)           # 內建 LED（可用來顯示狀態）
pwm = PWM(Pin(14), freq=50, duty=0)  # 伺服馬達控制腳位（GPIO14）

# I2C LCD 設定
i2c = I2C(1, freq=400000)
I2C_LCD = 0x27                        # LCD I2C 位址（可用 i2c.scan() 確認）
lcd = I2cLcd(i2c, I2C_LCD, 2, 16)     # 2行，16列 LCD
lcd.backlight_on()
lcd.clear()
# ================================

# 伺服馬達 PWM 參數（0度與180度的 duty 值）
d_min = 1638
d_span = 7864 - d_min

# WiFi 設定
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# GPIO_fakeV 目前未使用，可註解掉
# GPIO_fakeV = Pin(13, Pin.OUT)
# GPIO_fakeV.value(1)

# LED 閃爍參數
count = 360
cycleLen = 240
direction = 0


def mesg_come(topic, msg):
    """MQTT 訊息回呼函式 - 收到訊息時自動呼叫"""
    print((topic, msg))
    
    # 伺服馬達控制
    if topic == topic_servo:
        try:
            nn = int(msg)
        except:
            nn = -1       
        if nn >= 0 and nn < 181:
            # 將角度(0-180)轉換為 duty 值
            pwm.duty_u16(d_min + d_span * nn // 180)
    
    # LCD 顯示控制
    elif topic == topic_lcd:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(msg.decode())
    
    # 繼電器控制（低電位觸發）
    elif topic == topic_relay:
        if msg == b'H':
            GPIO_relay.value(0)  # LOW = 吸合（ON）
        elif msg == b'L':
            GPIO_relay.value(1)  # HIGH = 斷開（OFF）


def utc_cst():
    """取得台灣時間（UTC+8）"""
    cst = time.localtime(time.mktime(time.localtime()) + 28800)
    return "{0}/{1:02d}/{2:02d} {3:02d}:{4:02d}:{5:02d}".format(*cst)


def setTime():
    """同步 NTP 時間"""
    try:
        print("Setting time ...")
        ntptime.settime()
    except Exception as e:
        print(e)
    print(f"localtime->{utc_cst()}")


# ========== 主程式 ==========
try:
    # 連接 WiFi
    wifi.connect(WiFi_ssid, WiFi_password)
    print('start to connect wifi')
    for i in range(20):
        print(f'try to connect wifi in {i}s')
        time.sleep(1)
        if wifi.isconnected():
            print('WiFi connection OK!')
            print('Network Config=', wifi.ifconfig())
            break
    
    if not wifi.isconnected():
        print('WiFi connection Error')
        raise Exception('WiFi connection Error')

    # 同步時間
    setTime()
    
    # 連接 MQTT Broker
    mqttClient = MQTTClient(mqtt_client_id, mqtt_broker, port=mqtt_port, keepalive=65535)
    mqttClient.connect(False)  # False = 不清除會談資料
    mqttClient.set_callback(mesg_come)
    mqttClient.subscribe(topic=topic_all)
    
    old_tkms = 0
    
    # 主迴圈
    while 1:
        for j in range(count):
            for i in range(cycleLen):
                GPIO_led.value(direction ^ (0 if j >= i else 1))
            prn_log = mqttClient.check_msg()
            if prn_log:
                print(prn_log)
        direction = ~direction & 1
        print(f"localtime->{utc_cst()}")

except Exception as e:
    print(e)

pwm.deinit()