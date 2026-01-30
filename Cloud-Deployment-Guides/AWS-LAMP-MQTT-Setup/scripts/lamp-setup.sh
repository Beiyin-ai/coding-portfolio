#!/bin/bash
# AWS LAMP 一鍵安裝腳本
# 使用方法: bash lamp-setup.sh

echo "開始安裝 LAMP 服務..."

# 更新系統
sudo apt update && sudo apt upgrade -y

# 安裝 Apache
sudo apt install apache2 -y
sudo systemctl enable apache2
sudo systemctl start apache2

# 安裝 MySQL
sudo apt install mysql-server -y
sudo systemctl enable mysql
sudo systemctl start mysql

# 安裝 PHP
sudo apt install php libapache2-mod-php php-mysql php-cli php-curl php-gd php-json php-mbstring php-xml php-zip -y

# 啟用模組並重啟 Apache
sudo a2enmod rewrite
sudo systemctl restart apache2

# 測試安裝
echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/info.php

echo "安裝完成！"
echo "請訪問 http://<你的IP>/info.php 測試"
