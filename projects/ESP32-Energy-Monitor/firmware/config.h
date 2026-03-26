#ifndef CONFIG_H
#define CONFIG_H

// ==================== WiFi 設定 ====================
// extern const char* ssid;        // 加上 extern
// extern const char* password;    // 加上 extern
// extern const char* serverUrl;   // 加上 extern

// WiFi 設定結構
struct WiFiNetwork {
  const char* ssid;
  const char* password;
  const char* serverIp;
};

// 宣告外部變數（實際值寫在 config.cpp）
extern const WiFiNetwork knownNetworks[];
extern const int numNetworks;

// ==================== LED 燈條設定 ====================
#define LED_PIN       5
#define NUM_LEDS      8
#define LED_BRIGHTNESS 20
#define LED_UPDATE_MS 10000

// ==================== DHT22 設定 ====================
#define DHTPIN        27
#define DHTTYPE       DHT22

// ==================== 類比腳位設定 ====================
#define LDR_PIN       34
#define SOLAR_PIN     35
#define SOLAR_R1      10000.0
#define SOLAR_R2      10000.0

// ==================== OLED 設定 ====================
#define SCREEN_WIDTH  128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1

// ==================== 更新間隔 ====================
#define SENSOR_INTERVAL_MS 10000
#define OLED_UPDATE_MS     120000
#define WIFI_CHECK_MS      20000

// ==================== 功率閾值 ====================
#define POWER_LOW_MAX      200
#define POWER_MEDIUM_MAX   600

#endif