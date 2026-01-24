#!/usr/bin/env python3
"""
MQTT 發布者程式
課程：物聯網通訊實務 - 謝燿聰老師
功能：模擬終端機 mosquitto_pub 命令，發布測試訊息到 MQTT 主題
"""

import paho.mqtt.client as mqtt
import time
import sys

# 使用老師教材中的相同設定
mqtt_topic = "aiot-113/n26/h-t"
mqtt_broker = "127.0.0.1"
mqtt_port = 1883

def publish_single_message(client, message):
    """發布單一訊息"""
    result = client.publish(mqtt_topic, message)
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f"✅ 已發布: {message}")
        return True
    else:
        print(f"❌ 發布失敗: {message}")
        return False

def main():
    print("🚀 MQTT 發布者程式")
    print("=" * 40)
    print(f"主題: {mqtt_topic}")
    print(f"Broker: {mqtt_broker}:{mqtt_port}")
    print()
    
    client = mqtt.Client()
    
    try:
        # 連線到 Broker
        client.connect(mqtt_broker, mqtt_port, 60)
        print("✅ 連線成功")
        print()
        
        # 檢查命令列參數
        if len(sys.argv) > 1:
            # 使用命令列提供的訊息
            message = ' '.join(sys.argv[1:])
            publish_single_message(client, message)
        else:
            # 發布預設測試訊息
            test_messages = [
                "69.1 31.1",  # 老師的範例
                "25.5 60.0",  # 溫度濕度
                "Hello MQTT", # 文字訊息
                "測試結束"     # 結束標記
            ]
            
            for i, msg in enumerate(test_messages, 1):
                print(f"測試 {i}: {msg}")
                publish_single_message(client, msg)
                time.sleep(1)  # 等待 1 秒
            
            print()
            print("✅ 所有測試訊息已發布")
        
        print()
        print("📋 終端機測試指令參考：")
        print(f"mosquitto_pub -h {mqtt_broker} -p {mqtt_port} -t {mqtt_topic} -m '你的訊息'")
        
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
