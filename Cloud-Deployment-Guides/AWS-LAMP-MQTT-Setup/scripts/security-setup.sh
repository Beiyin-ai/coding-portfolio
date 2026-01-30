#!/bin/bash
# 基礎安全設定腳本

echo "設定基礎安全..."

# 更新系統
sudo apt update && sudo apt upgrade -y

# 安裝防火牆
sudo apt install ufw -y
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 開放必要端口
sudo ufw allow 22/tcp  # SSH
sudo ufw allow 80/tcp  # HTTP
sudo ufw allow 443/tcp # HTTPS
sudo ufw allow 1883/tcp # MQTT

# 啟用防火牆
sudo ufw --force enable

# 顯示防火牆狀態
sudo ufw status verbose

echo "安全設定完成！"
