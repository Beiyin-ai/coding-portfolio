# MQTT 測試指令

## 📋 前置設定
```bash
# 設定主題前綴
YourTopicHead=your/topic/prefix

# MQTT Broker 設定
BROKER="************"
PORT=443
```

## 🔌 繼電器控制
```bash
# 開啟繼電器（H）
mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/relay -m H

# 關閉繼電器（L）
mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/relay -m L
```

## 📺 LCD 顯示
```bash
# 顯示一般文字
mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/LCD -m "Hello World"

# 顯示16字元以內的訊息
mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/LCD -m "Mid Autumn Festival"

# 顯示英文訊息
mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/LCD -m "Merry Christmas"
```

## 🎯 伺服馬達控制
```bash
# 轉到指定角度（0-180度）
mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/servo -m 32
mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/servo -m 122
mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/servo -m 1
mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/servo -m 179
```

## 📡 監聽所有訊息
```bash
# 在另一個終端機執行
mosquitto_sub -h $BROKER -p $PORT -t $YourTopicHead/#
```

## 🐳 Docker 方式（如果沒有安裝 mosquitto）
```bash
# 啟動 MQTT Broker 容器
docker run -d --name my-mqtt -p 1883:1883 -p 9001:9001 eclipse-mosquitto:2.0

# 透過 docker 執行指令
docker exec my-mqtt mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/servo -m 32
docker exec my-mqtt mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/LCD -m "Hello"
docker exec my-mqtt mosquitto_pub -h $BROKER -p $PORT -t $YourTopicHead/relay -m H
```
