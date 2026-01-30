#!/usr/bin/env python3
# MQTT 發布者範例

import paho.mqtt.client as mqtt
import time

# MQTT 伺服器設定
MQTT_BROKER = "localhost"  # 改為你的 EC2 IP
MQTT_PORT = 1883
TOPIC = "home/sensor/temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("連線成功")
    else:
        print(f"連線失敗，錯誤碼: {rc}")

# 建立 MQTT 用戶端
client = mqtt.Client()
client.on_connect = on_connect

# 連線到 MQTT Broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

# 發布訊息
try:
    for i in range(10):
        message = f"溫度: {20 + i}°C"
        client.publish(TOPIC, message)
        print(f"已發布: {message}")
        time.sleep(1)
except KeyboardInterrupt:
    print("中斷發布")
finally:
    client.loop_stop()
    client.disconnect()
