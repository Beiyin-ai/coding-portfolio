# 疑難排解指南

## 📡 WiFi 連線問題

### Q: ESP32 無法連線到 WiFi
**可能原因：**
- WiFi 名稱或密碼錯誤
- WiFi 訊號太弱
- ESP32 天線問題

**解決方法：**
1. 確認 `main.py` 中的 WiFi_ssid 和 WiFi_password 是否正確
2. 檢查 ESP32 是否在 WiFi 覆蓋範圍內
3. 重啟 ESP32 重新嘗試連線
4. 在序列監控視窗查看錯誤訊息

```python
# 檢查程式碼中的 WiFi 設定
WiFi_ssid = "你的WiFi名稱"     # 確認是否正確
WiFi_password = "你的WiFi密碼" # 確認是否正確
```

---

## 🔌 MQTT 連線問題

### Q: ESP32 無法連線到 MQTT Broker
**可能原因：**
- MQTT Broker IP 或埠號錯誤
- MQTT Broker 未啟動
- 防火牆阻擋連線

**解決方法：**
1. 確認 `config.json` 中的 MQTT 設定正確
2. 用 `mosquitto_pub` 測試 Broker 是否正常運作
3. 檢查 Broker 的 IP 是否與 ESP32 在同一網段

```bash
# 測試 MQTT Broker 是否正常
mosquitto_pub -h 你的BrokerIP -p 443 -t test -m "hello" -d
```

### Q: 收不到 MQTT 訊息
**可能原因：**
- 訂閱的主題（topic）與發佈的不一致
- 權限設定錯誤

**解決方法：**
1. 確認 `topic_head` 設定是否一致
2. 用 `mosquitto_sub` 訂閱所有主題測試

```bash
# 監聽所有訊息，確認主題是否正確
mosquitto_sub -h 你的BrokerIP -p 443 -t your/topic/#
```

---

## 💡 LED 問題

### Q: LED 不亮
**可能原因：**
- GPIO 腳位錯誤
- LED 極性接反
- LED 燒壞（未串接電阻）

**解決方法：**
1. 確認 LED 正極（長腳）接對 GPIO
2. 確認 LED 負極（短腳）接 GND
3. ⚠️ **務必串接 220Ω～330Ω 電阻，否則會燒壞 LED 或 GPIO**

### Q: LED 非常暗
**可能原因：**
- 電阻阻值太大
- GPIO 電壓不足

**解決方法：**
1. 改用 220Ω 電阻
2. 確認 GPIO 有輸出 3.3V

---

## 🔧 繼電器問題

### Q: 繼電器無動作
**可能原因：**
- 接線錯誤
- 觸發邏輯錯誤（高電位/低電位）
- 電源不足

**解決方法：**
1. 確認繼電器 VCC 接 5V，GND 接 GND
2. 本系統使用 **低電位觸發**，程式邏輯為：
   - `relay.value(0)` → 吸合（ON）
   - `relay.value(1)` → 斷開（OFF）
3. 檢查電源是否足夠驅動繼電器

### Q: 繼電器一直吸合
**可能原因：**
- GPIO 初始狀態錯誤
- 程式未正確控制

**解決方法：**
1. 開機時先將 GPIO 設為 HIGH
2. 在 `main.py` 加入初始化：`relay.value(1)`

---

## 🦾 伺服馬達問題

### Q: 伺服馬達不動
**可能原因：**
- 電源不足
- PWM 腳位錯誤
- 頻率設定錯誤

**解決方法：**
1. 伺服馬達需接 **5V**，不可接 3.3V
2. 確認訊號線接對 GPIO（本系統使用 GPIO14）
3. 確認 PWM 頻率為 50Hz
4. 檢查共地：伺服馬達 GND 必須與 ESP32 GND 相連

```python
# 正確的 PWM 設定
pwm = PWM(Pin(14), freq=50, duty=0)
```

### Q: 伺服馬達抖動或位置不準
**可能原因：**
- 電源不穩
- PWM 計算錯誤

**解決方法：**
1. 使用獨立電源或加大電容
2. 校正 d_min 和 d_span 數值

---

## 📺 LCD 顯示問題

### Q: LCD 無顯示
**可能原因：**
- I2C 位址錯誤
- 接線錯誤
- 對比度調整不當

**解決方法：**
1. 掃描 I2C 裝置確認位址：
   ```python
   from machine import I2C, Pin
   i2c = I2C(1, freq=400000)
   print(i2c.scan())  # 應該顯示 [0x27] 或 [0x3F]
   ```
2. 確認 SDA 接 GPIO12，SCL 接 GPIO26
3. 調整 LCD 背面的可變電阻調整對比度

### Q: LCD 顯示亂碼
**可能原因：**
- I2C 通訊不穩
- 初始化順序錯誤

**解決方法：**
1. 降低 I2C 頻率試試
2. 檢查接線是否鬆動
3. 重啟 ESP32

---

## ⏰ 時間同步問題

### Q: NTP 時間同步失敗
**可能原因：**
- WiFi 未連線
- NTP 伺服器無法連線

**解決方法：**
1. 確認 WiFi 已連線
2. 改用其他 NTP 伺服器：
   ```python
   ntptime.host = "pool.ntp.org"  # 或 "time.google.com"
   ```

### Q: 顯示的時間不正確
**可能原因：**
- 時區設定錯誤

**解決方法：**
1. 台灣時間為 UTC+8，程式已自動轉換
2. 如需其他時區，修改 `utc_cst()` 函式中的 +28800 秒（8小時）

---

## 📝 其他常見問題

### Q: ESP32 一直重啟
**可能原因：**
- 電源不穩
- 程式有未捕獲的例外

**解決方法：**
1. 使用穩定電源（如 5V/2A 變壓器）
2. 在序列監控視窗查看錯誤訊息
3. 用 try-except 捕獲可能的例外

### Q: 上傳程式到 ESP32 失敗
**可能原因：**
- 序列埠被占用
- 沒有按燒錄按鈕

**解決方法：**
1. 關閉其他占用序列埠的程式（如序列監控視窗）
2. 上傳時按住 ESP32 的 BOOT 按鈕
3. 確認使用的序列埠正確（/dev/ttyUSB0 或 COM3）

---

## 📞 尋求協助

如果以上方法都無法解決你的問題：

1. 開啟 GitHub Issue，附上：
   - 錯誤訊息（序列監控視窗的輸出）
   - 你的 `main.py` 和 `config.json`（記得隱藏密碼）
   - 接線照片

2. 檢查 [GitHub 專案 Issues](https://github.com/Beiyin-ai/coding-portfolio/issues) 是否有類似問題