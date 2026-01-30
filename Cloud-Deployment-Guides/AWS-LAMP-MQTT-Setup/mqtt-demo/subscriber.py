#!/usr/bin/env python3
# MQTT 訂閱者範例

import paho.mqtt.client as mqtt

# MQTT 伺服器設定
MQTT_BROKER = "localhost"  # 改為你的 EC2 IP
MQTT_PORT = 1883
TOPIC = "home/sensor/temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("連線成功")
        client.subscribe(TOPIC)
        print(f"已訂閱主題: {TOPIC}")
    else:
        print(f"連線失敗，錯誤碼: {rc}")

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

# 建立 MQTT 用戶端
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# 連線到 MQTT Broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# 保持連線並接收訊息
try:
    print("開始監聽訊息... 按 Ctrl+C 結束")
    client.loop_forever()
except KeyboardInterrupt:
    print("中斷訂閱")
    client.disconnect()
