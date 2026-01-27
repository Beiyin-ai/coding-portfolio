import network, time
from machine import Pin, I2C
import ssd1306
import dht
from umqtt.simple import MQTTClient

# === WiFi 設定 ===
ssid = "你的WIFI名稱"
password = "你的WIFI密碼"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    print("Connecting WiFi...")
    time.sleep(1)

print("WiFi connected:", sta_if.ifconfig())

# === OLED 初始化 ===
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# === DHT22 初始化 ===
dht_sensor = dht.DHT22(Pin(4))

# === 按鈕初始化 ===
button = Pin(23, Pin.IN, Pin.PULL_UP)

def button_pressed():
    if button.value() == 0:
        time.sleep_ms(50)
        if button.value() == 0:
            while button.value() == 0:
                pass
            return True
    return False

# === MQTT Broker 設定 ===
mqtt_server = "test.mosquitto.org"
client_id = "esp32_oled"
topic_sub = b"pei/oled"
message_text = ""

def sub_cb(topic, msg):
    global message_text
    message_text = msg.decode()
    print("Got message:", message_text)

client = MQTTClient(client_id, mqtt_server)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic_sub)

# === 畫面狀態 ===
screen_mode = 0   # 0=日期+溫溼度, 1=訊息畫面, 2=倒數頁面
last_switch_time = time.time()

# === 特殊日期設定 ===
special_dates = {
    "0113": "Happy Birthday!",
    "0716": "My Birthday!",
    "0515": "Anniversary!"
}

# === 簡單動畫效果 ===
def blink_text(text, times=3):
    for i in range(times):
        oled.fill(0)
        oled.text(text, 0, 20)
        oled.show()
        time.sleep(0.5)
        oled.fill(0)
        oled.show()
        time.sleep(0.5)

# === 倒數日期功能 ===
def days_until(month, day):
    today = time.localtime()
    target = time.mktime((today[0], month, day, 0, 0, 0, 0, 0))
    now = time.mktime(today)
    diff = int((target - now) / 86400)
    return diff if diff >= 0 else None

def show_countdowns(oled, skip_last=False):
    events = [
        ("Bear", 1, 13),
        ("Baby", 7, 16),
        ("<3", 5, 15)
    ]
    y = 0
    nearest_name = None
    nearest_days = None

    for name, m, d in events:
        days = days_until(m, d)
        if days is not None and days <= 7:
            oled.text("{} in {} days".format(name, days), 0, y)
        elif days is not None:
            oled.text("{} {:02d}-{:02d}".format(name, m, d), 0, y)
        else:
            oled.text("{} {:02d}-{:02d}".format(name, m, d), 0, y)
        y += 16

        if days is not None:
            if nearest_days is None or days < nearest_days:
                nearest_days = days
                nearest_name = name

    if not skip_last and nearest_name is not None:
        oled.text("Next {} in {} days".format(nearest_name, nearest_days), 0, 48)

    return nearest_name, nearest_days

def marquee_text(oled, text, y=48, speed=4):
    width = len(text) * 8
    for x in range(0, 128 + width, speed):
        oled.fill(0)
        show_countdowns(oled, skip_last=True)
        oled.text(text, 128 - x, y)
        oled.show()
        time.sleep(0.1)

# === 主迴圈 ===
while True:
    client.check_msg()

    today = time.localtime()
    date_str = "{:02d}{:02d}".format(today[1], today[2])
    full_date = "{:04d}-{:02d}-{:02d}".format(today[0], today[1], today[2])
    full_time = "{:02d}:{:02d}:{:02d}".format(today[3], today[4], today[5])

    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
    except:
        temp, hum = 0, 0

    # 按鈕切換畫面
    if button_pressed():
        screen_mode = (screen_mode + 1) % 3
        last_switch_time = time.time()

    # 自動回到第一頁 (例如 10 秒)
    if screen_mode in (1, 2) and (time.time() - last_switch_time > 10):
        screen_mode = 0

    oled.fill(0)
    if screen_mode == 0:
        special_msg = special_dates.get(date_str)
        if special_msg:
            blink_text(special_msg, 5)
        else:
            oled.text(full_date, 0, 0)       # 第 1 行
            oled.text(full_time, 0, 16)      # 第 2 行
            oled.text("Temp:{}C".format(temp), 0, 32)  # 第 3 行
            oled.text("Hum:{}%".format(hum), 0, 48)    # 第 4 行

    elif screen_mode == 1:
        oled.text("Msg:", 0, 0)
        oled.text(message_text[:16], 0, 20)
        oled.text(message_text[16:32], 0, 40)

    elif screen_mode == 2:
        nearest_name, nearest_days = show_countdowns(oled)
        oled.show()
        time.sleep(2)
        if nearest_name is not None:
            marquee_text(oled, "Next {} in {} days".format(nearest_name, nearest_days), y=48)

    oled.show()
    time.sleep(0.2)
