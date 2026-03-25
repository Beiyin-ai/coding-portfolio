# 接線說明

| 裝置 | 腳位 | 說明 |
|------|------|------|
| LED 燈條 | GPIO5 | DATA 線 |
| INA219 | GPIO21(SDA), GPIO22(SCL) | I2C |
| DHT22 | GPIO27 | DATA 線 + 10K 上拉 |
| 光敏電阻 | GPIO34 | 分壓電路 (10K 電阻) |
| 太陽能板 | GPIO35 | 分壓電路 (10K+10K) |
| OLED | GPIO21(SDA), GPIO22(SCL) | I2C |

## 電源
- ESP32: 電腦 USB 供電
- LED 燈條: 手機充電頭 5V (需共地)
