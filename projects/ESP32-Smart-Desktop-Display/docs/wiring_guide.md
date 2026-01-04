# ESP32 Smart Desktop Display 接線指南

## 接線圖

請參考 images/circuit_diagram.png

## 詳細接線說明

| ESP32 腳位 | 連接元件 | 腳位說明 |
|------------|----------|----------|
| 3.3V | OLED VCC, DHT22 VCC, WS2812B VDD | 電源正極 |
| GND | OLED GND, DHT22 GND, WS2812B VSS, Button | 接地 |
| GPIO21 | OLED SDA | I2C 資料線 |
| GPIO22 | OLED SCL | I2C 時鐘線 |
| GPIO4 | DHT22 DATA | 溫濕度資料線 |
| GPIO13 | WS2812B DIN | LED 資料輸入 |
| GPIO15 | Button | 按鈕輸入 (內部上拉) |

## 注意事項
1. 請確保電源正負極連接正確
2. DHT22 的資料腳需要連接 4.7kΩ 上拉電阻
3. WS2812B LED 的資料輸入方向要正確
