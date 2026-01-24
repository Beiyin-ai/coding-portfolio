import paho.mqtt.client as mqtt

#  終端機測試：   👉 mosquitto_pub  -h 49.158.45.134  -p 80    -t  aiot-113/n26/h-t    -m '69.1 31.1'
mqtt_topic = "aiot-113/n26/h-t"  # 訂閱 subscribe ，設 主題 topic ：aiot-113/n26/h-t  ， n26 改成 iot-xx ，xx 是您的座號

mqtt_broker = "127.0.0.1"  # MQTT代理人 IP （  broker server ）
mqtt_port = 1883                 # MQTT代理人 port（  broker server ）


def my_onConnect(client, userdata, flags, rc):       # 與MQTT代理人連上線時 的 回呼函數 callback function
    print("Connected with result code " + str(rc))
    client.subscribe(mqtt_topic)                      # 訂閱 主題 

def my_onMessage(client, userdata, msg):              # 收到訊息時 的 回呼函數 callback function
    print("[{}]: {}".format(msg.topic, str(msg.payload)))

mqtt_client = mqtt.Client()
mqtt_client.on_connect = my_onConnect  # 連上線時的回呼函數 callback function
mqtt_client.on_message = my_onMessage  # 設定 收到訊息時的回呼函數 callback function

mqtt_client.connect( mqtt_broker, mqtt_port)  

mqtt_client.loop_forever()
