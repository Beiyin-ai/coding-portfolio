# 硬體接線說明

## ⚠️ 重要注意事項

### LED 無電阻風險
目前 LED 沒有串接限流電阻，**存在燒毀 GPIO 風險**。

建議每顆 LED 串接 220Ω～330Ω 電阻：
```
GPIO ── 電阻 ── LED ── GND
```

### Relay 低電位觸發
本系統使用 **低電位觸發** 繼電器：
- GPIO = LOW (0) → Relay 吸合（ON）
- GPIO = HIGH (1) → Relay 斷開（OFF）

開機時建議先將 GPIO 設為 HIGH，避免誤動作。

---

## 一、電源與共地

| ESP32 腳位 | 連接目標 | 說明 |
|-----------|---------|------|
| VIN (5V) | 麵包板 5V 電源軌 | 提供 5V 電源給 Relay、Servo、LCD |
| 3.3V | 麵包板 3.3V 電源軌 | 提供 3.3V 電源（目前未使用） |
| GND | 麵包板 GND 電源軌 | 所有模組共地 |

**所有模組的 GND 都必須接到同一條 GND 軌道，與 ESP32 共地。**

---

## 二、LED 指示燈

| LED | ESP32 腳位 | 負極連接 | 備註 |
|-----|-----------|---------|------|
| 紅色 LED | GPIO25 | GND | ⚠️ 需串接 220Ω～330Ω 電阻 |
| 綠色 LED | GPIO26 | GND | ⚠️ 需串接 220Ω～330Ω 電阻 |

用途：顯示系統狀態（例如辨識失敗/成功）

---

## 三、Relay 繼電器模組

### 控制腳位（低電位觸發）
| Relay 腳位 | 連接目標 | 說明 |
|-----------|---------|------|
| S (Signal) | ESP32 GPIO13 | 控制訊號（LOW=ON, HIGH=OFF） |
| + (VCC) | 5V 電源軌 | 繼電器模組供電 |
| - (GND) | GND 電源軌 | 共地 |

### 負載接點（高壓側）
| 接點 | 說明 |
|-----|------|
| COM | 公共端 |
| NO | 常開（Normal Open） |
| NC | 常閉（Normal Close） |

---

## 四、Servo 伺服馬達

| Servo 線色 | 連接目標 | 說明 |
|-----------|---------|------|
| 紅線 | 5V 電源軌 | 馬達電源（**不可接 3.3V**） |
| 棕/黑線 | GND 電源軌 | 共地 |
| 黃/橘線 | ESP32 GPIO14 | 控制訊號（PWM） |

---

## 五、LCD 顯示器（I2C 介面）

| LCD 腳位 | 連接目標 | 說明 |
|---------|---------|------|
| GND | GND 電源軌 | 共地 |
| VCC | 5V 電源軌 | LCD 供電（5V） |
| SDA | ESP32 GPIO12 | I2C 資料線 |
| SCL | ESP32 GPIO26 | I2C 時脈線 |

---

## 六、GPIO 對照總表

| 功能 | ESP32 腳位 | 備註 |
|------|-----------|------|
| 紅色 LED | GPIO25 | ⚠️ 需串接電阻 |
| 綠色 LED | GPIO26 | ⚠️ 需串接電阻 |
| Relay 控制 | GPIO13 | 低電位觸發（LOW=ON） |
| Servo 控制 | GPIO14 | PWM 訊號 |
| LCD SDA | GPIO12 | I2C 資料線 |
| LCD SCL | GPIO26 | I2C 時脈線 |
| 5V 電源 | VIN | 供電給 Relay、Servo、LCD |
| 3.3V 電源 | 3.3V | 備用 |
| GND | GND | 所有模組共地 |

---

## 七、風險評估與修正建議

| 項目 | 目前狀態 | 風險 | 建議 |
|------|---------|------|------|
| LED | 無電阻 | ❌ 高風險 | 每顆串接 220Ω～330Ω 電阻 |
| Relay | 低電位觸發 | ⚠️ 程式注意 | 開機先設 HIGH，避免誤動作 |
| LCD | 5V 供電 | ✅ 安全 | 無 |
| Servo | GPIO14 控制 | ✅ 安全 | 確認共地 |

---

## 八、對應程式碼範例

```python
from machine import Pin, PWM

# LED（需先串接電阻）
led_red = Pin(25, Pin.OUT)
led_green = Pin(26, Pin.OUT)

# Relay（低電位觸發）
relay = Pin(13, Pin.OUT)
relay.value(1)  # 開機先設 HIGH，避免誤動作

# 開啟 Relay（LOW 觸發）
relay.value(0)  # ON
relay.value(1)  # OFF

# Servo（GPIO14）
servo = PWM(Pin(14), freq=50)
servo.duty_u16(1638 + (7864-1638) * angle // 180)
```
