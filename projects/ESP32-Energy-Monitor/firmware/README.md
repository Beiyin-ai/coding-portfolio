# ESP32 能源監控系統 - 設定說明

## ⚙️ 設定檔說明

### 【WiFi帳密】→ 改 `config.cpp`
```cpp
const char* ssid = "AIMESH92";        // ← 改成您的WiFi名稱
const char* password = "92abcd1234";  // ← 改成您的WiFi密碼
```

### 【伺服器網址】→ 改 `config.cpp`
```cpp
const char* serverUrl = "http://192.168.50.143:5000/api/sensor-data";
```
> **📌 要看電腦IP的方法：**
> - **Windows**: 打開cmd → 輸入 `ipconfig` → 找 **IPv4 地址**
> - **Mac**: 系統偏好設定 → 網路
>
> *例如：IPv4 地址是 192.168.1.100 → 網址就是 `http://192.168.1.100:5000/api/sensor-data`*

### 【腳位定義】→ 改 `config.h`
```cpp
#define LED_PIN       5      // LED 燈條
#define DHTPIN        27     // DHT22 溫濕度感測器
#define LDR_PIN       34     // 光敏電阻
#define SOLAR_PIN     35     // 太陽能板電壓
```

### 【LED顏色】→ 改 `led_controller.cpp`
```cpp
#define PINK_R 255     // 紅色數值 (0-255)
#define PINK_G 105     // 綠色數值 (0-255)  
#define PINK_B 180     // 藍色數值 (0-255)
```
> 🎨 想要其他顏色可以上網搜尋 **"RGB顏色對照表"**

### 【LED亮度】→ 改 `led_controller.cpp`
```cpp
#define LED_BRIGHTNESS 20   // 亮度 (0-255)，數值越大越亮
```

### 【更新頻率】→ 改 `config.h`
```cpp
#define SENSOR_INTERVAL_MS 10000   // 感測器讀取間隔 = 10秒
#define OLED_UPDATE_MS 120000      // OLED更新間隔 = 10分鐘
#define WIFI_CHECK_MS 20000        // WiFi檢查間隔 = 20秒
#define LED_UPDATE_MS 10000        // LED更新間隔 = 10秒
```

### 【裝置ID】→ 改 `data_upload.cpp`
```cpp
doc["device_id"] = "ESP32_01";  // 可以改成您想要的名稱
```

---

## ⚠️ **重要提醒**

### 🔴 **注意1：`config.h` 裡面有 `extern` 開頭的不要改數值！**
```cpp
extern const char* ssid;  // ← 這是宣告，不要在這裡給值
```

### 🟡 **注意2：要改 WiFi、密碼、網址，請去 `config.cpp`**
```cpp
const char* ssid = "您的WiFi";  // ← 這才是真正給值的地方
```

### 🟢 **注意3：修改完檔案要按 Ctrl+S 存檔，再按上傳**

---

## ❓ **常見問題**

❌ **編譯錯誤：multiple definition**
→ 表示您改到 `config.h` 了，數值要改在 `config.cpp`

❌ **WiFi 連不上**
→ 檢查 `config.cpp` 裡的 ssid 和 password 是否正確
→ 檢查電腦的 IP 有沒有改變

❌ **OLED 沒顯示**
→ 檢查 OLED_UPDATE_MS 數值是否太大
→ 檢查腳位連接是否正確

❌ **感測器讀不到**
→ 檢查 `config.h` 裡的腳位定義是否正確
→ 檢查硬體接線

---

## 🔗 **快捷指令**

**查電腦IP：**
- Windows: 按 Win+R → 輸入 `cmd` → 輸入 `ipconfig`
- Mac: 系統偏好設定 → 網路

**顏色查詢：**
https://www.rapidtables.com/web/color/RGB_Color.html

---

📅 **最後更新：2024/03/19**