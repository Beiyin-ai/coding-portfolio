#!/bin/bash
# MQTT 一鍵安裝腳本

echo "安裝 Mosquitto MQTT Broker..."
sudo apt install mosquitto mosquitto-clients -y

# 設定 MQTT 允許匿名連線
sudo cp /etc/mosquitto/mosquitto.conf /etc/mosquitto/mosquitto.conf.backup
echo -e "allow_anonymous true\nlistener 1883 0.0.0.0" | sudo tee /etc/mosquitto/mosquitto.conf

# 重啟服務
sudo systemctl restart mosquitto
sudo systemctl enable mosquitto

echo "安裝完成！"
echo "測試訂閱: mosquitto_sub -h localhost -t test -v"
echo "測試發布: mosquitto_pub -h localhost -t test -m \"Hello MQTT\""
