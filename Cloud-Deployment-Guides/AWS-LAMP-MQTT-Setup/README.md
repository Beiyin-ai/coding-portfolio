# AWS 雲端架站與 MQTT 服務部署指南

本指南詳細說明如何在 AWS EC2 上部署 LAMP 環境（Linux + Apache + MySQL + PHP）並安裝 MQTT 服務，適用於 IoT 專案或網站後端部署。

## 📋 目錄
1. [AWS 帳號註冊與登入](#1-aws-帳號註冊與登入)
2. [啟動 EC2 執行個體](#2-啟動-ec2-執行個體)
3. [設定安全群組（防火牆）](#3-設定安全群組防火牆)
4. [SSH 遠端連線與系統更新](#4-ssh-遠端連線與系統更新)
5. [安裝 LAMP 服務](#5-安裝-lamp-服務)
6. [部署 PHP 網站](#6-部署-php-網站)
7. [安裝與設定 MQTT（Mosquitto）](#7-安裝與設定-mqttmosquitto)
8. [固定 IP 與域名設定](#8-固定-ip-與域名設定)
9. [資料庫設定（MySQL）](#9-資料庫設定mysql)
10. [檔案傳輸與管理](#10-檔案傳輸與管理)

---

## 1. AWS 帳號註冊與登入

### 步驟概要：
1. 前往 [AWS 官網](https://aws.amazon.com/) 註冊帳號
2. 完成手機驗證與付款資訊設定（有免費方案）
3. 登入 AWS Management Console

### 注意事項：
- 使用完畢請記得登出，避免產生額外費用
- 免費方案有使用限制，請注意用量

---

## 2. 啟動 EC2 執行個體

### 選擇作業系統（AMI）
```bash
# 建議選擇 Ubuntu 24.04 LTS
# AMI ID: ami-0c55b159cbfafe1f0（us-east-1）
```

### 執行個體類型
- 免費方案：t2.micro（1 vCPU, 1 GB RAM）
- 測試用：t2.small（1 vCPU, 2 GB RAM）

### 儲存空間設定
```bash
# 預設 8GB，建議調整為 20GB 以利後續安裝
```

---

## 3. 設定安全群組（防火牆）

必須開啟以下 Port：

| Port | 協定 | 用途 | 來源 |
|------|------|------|------|
| 22 | TCP | SSH 遠端連線 | 0.0.0.0/0（或指定 IP） |
| 80 | TCP | HTTP 網頁服務 | 0.0.0.0/0 |
| 443 | TCP | HTTPS 加密連線 | 0.0.0.0/0 |
| 1883 | TCP | MQTT 通訊協定 | 0.0.0.0/0 |

### 指令檢查安全群組：
```bash
# 檢視執行個體狀態
aws ec2 describe-instances --instance-ids <你的執行個體ID>

# 檢視安全群組規則
aws ec2 describe-security-groups --group-ids <你的安全群組ID>
```

---

## 4. SSH 遠端連線與系統更新

### 使用 SSH 金鑰連線：
```bash
# 下載金鑰檔（.pem）
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@<你的EC2公有IP>
```

### 首次連線後更新系統：
```bash
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y
```

---

## 5. 安裝 LAMP 服務

### 5.1 安裝 Apache
```bash
sudo apt install apache2 -y
sudo systemctl enable apache2
sudo systemctl start apache2
```

### 5.2 安裝 MySQL
```bash
sudo apt install mysql-server -y
sudo systemctl enable mysql
sudo systemctl start mysql

# 安全性設定
sudo mysql_secure_installation
```

### 5.3 安裝 PHP
```bash
sudo apt install php libapache2-mod-php php-mysql php-cli php-curl php-gd php-json php-mbstring php-xml php-zip -y

# 啟用 Apache rewrite 模組
sudo a2enmod rewrite
sudo systemctl restart apache2
```

### 5.4 測試安裝
```bash
# 建立測試頁面
echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/info.php

# 瀏覽器訪問：
# http://<你的EC2公有IP>/info.php
```

---

## 6. 部署 PHP 網站

### 設定網站目錄權限：
```bash
# 建立網站目錄
sudo mkdir -p /var/www/html/myweb

# 更改擁有者為 ubuntu 使用者
sudo chown -R $USER:$USER /var/www/html/
sudo chmod -R 755 /var/www/html/

# 建立範例頁面
cat > /var/www/html/myweb/index.php << 'PHP_EOF'
<html>
<head>
    <title>我的 AWS 網站</title>
</head>
<body>
    <?php
        echo "<p>PHP 執行時間：" . date('Y-m-d H:i:s') . "</p>";
        echo "<p>伺服器：" . $_SERVER['SERVER_SOFTWARE'] . "</p>";
    ?>
</body>
</html>
PHP_EOF
```

### 測試網站：
```
http://<你的EC2公有IP>/myweb/
```

---

## 7. 安裝與設定 MQTT（Mosquitto）

### 7.1 安裝 Mosquitto Broker
```bash
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### 7.2 設定 Mosquitto
```bash
# 備份原始設定檔
sudo cp /etc/mosquitto/mosquitto.conf /etc/mosquitto/mosquitto.conf.backup

# 編輯設定檔
sudo nano /etc/mosquitto/mosquitto.conf
```

#### 重要設定：
```
# 允許匿名連線（測試用）
allow_anonymous true

# 監聽所有網路介面
listener 1883 0.0.0.0

# 啟用日誌
log_dest file /var/log/mosquitto/mosquitto.log
log_type all
```

### 7.3 重啟服務
```bash
sudo systemctl restart mosquitto
sudo systemctl status mosquitto
```

### 7.4 MQTT 測試
#### 訂閱端：
```bash
mosquitto_sub -h localhost -t "test/topic" -v
```

#### 發布端：
```bash
mosquitto_pub -h localhost -t "test/topic" -m "Hello MQTT from AWS"
```

---

## 8. 固定 IP 與域名設定

### 申請 Elastic IP：
1. 進入 AWS Console → EC2 → Elastic IPs
2. 點擊 "Allocate Elastic IP address"
3. 分配後關聯到你的 EC2 執行個體

### 設定 DNS（範例）：
```bash
# 如果使用 Route 53 或其它 DNS 服務
# 將域名指向你的 Elastic IP
# 例如：your-domain.com → 34.203.35.40
```

---

## 9. 資料庫設定（MySQL）

### 建立資料庫與使用者：
```bash
# 登入 MySQL
sudo mysql -u root

# 在 MySQL 內執行
CREATE DATABASE myapp_db;
CREATE USER 'myapp_user'@'%' IDENTIFIED BY '你的密碼';
GRANT ALL PRIVILEGES ON myapp_db.* TO 'myapp_user'@'%';
FLUSH PRIVILEGES;
EXIT;
```

### 建立測試表格：
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 10. 檔案傳輸與管理

### 使用 WinSCP（Windows）：
1. 下載 WinSCP：https://winscp.net/
2. 設定連線：
   - 協定：SCP
   - 主機：你的 EC2 公有 IP
   - 使用者：ubuntu
   - 私密金鑰：匯入你的 .pem 檔

### 使用 scp 指令（Linux/Mac）：
```bash
# 上傳檔案
scp -i your-key.pem local-file.txt ubuntu@<你的EC2 IP>:~/remote-path/

# 下載檔案
scp -i your-key.pem ubuntu@<你的EC2 IP>:~/remote-file.txt ./
```

---

## 🔧 疑難排解

### Apache 無法啟動：
```bash
sudo systemctl status apache2
sudo journalctl -xeu apache2
```

### MQTT 無法連線：
```bash
# 檢查 Port 1883 是否開啟
sudo netstat -tlnp | grep 1883

# 檢查防火牆
sudo ufw status
```

### MySQL 連線問題：
```bash
# 檢查綁定位址
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
# 確認 bind-address = 0.0.0.0
```

---

## 📊 服務狀態檢查指令

```bash
# 檢查所有服務狀態
sudo systemctl status apache2 mysql mosquitto

# 檢查磁碟空間
df -h

# 檢查記憶體使用
free -h

# 檢查網路連線
sudo netstat -tulpn
```

---

## 🎯 快速部署腳本

參考 `scripts/` 目錄下的自動化腳本：
- `lamp-setup.sh` - 一鍵安裝 LAMP
- `mqtt-setup.sh` - 安裝與設定 MQTT
- `security-setup.sh` - 基礎安全設定

---

## 📝 後續學習建議

1. **容器化部署**：使用 Docker 打包應用程式
2. **自動化部署**：使用 Ansible/Terraform
3. **監控與日誌**：CloudWatch、Grafana
4. **負載平衡**：AWS ELB
5. **資料庫備份**：自動化備份策略

---

## 📚 參考資源

- [AWS EC2 官方文件](https://docs.aws.amazon.com/ec2/)
- [Ubuntu 官方指南](https://ubuntu.com/tutorials)
- [Mosquitto 文件](https://mosquitto.org/documentation/)
- [PHP 官方文件](https://www.php.net/docs.php)

---

## ⚠️ 注意事項

1. **費用控制**：記得關閉不需要的服務
2. **安全最佳實踐**：
   - 定期更新系統
   - 使用強密碼
   - 限制 SSH 來源 IP
   - 定期備份重要資料
3. **測試環境**：先在免費方案測試，再部署到正式環境

---

**最後更新：2026年1月30日**  
如有問題或建議，歡迎提出 Issue 或 Pull Request！
