#include <Wire.h>
#include <Adafruit_INA219.h>
#include <Adafruit_NeoPixel.h>
#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

// ==================== 設定區 ====================
// WiFi
const char* ssid     = "kbro-51-28";
const char* password = "0937696881";
const char* serverUrl = "http://192.168.0.46:5000/api/sensor-data";

// LED 燈條
#define LED_PIN       5
#define NUM_LEDS      8
#define LED_BRIGHTNESS 20
#define LED_UPDATE_MS 10000      // LED 動畫更新間隔 (ms)

// INA219
Adafruit_INA219 ina219;

// DHT22
#define DHTPIN        27
#define DHTTYPE       DHT22
DHT dht(DHTPIN, DHTTYPE);

// 光敏電阻
#define LDR_PIN       34

// 太陽能板分壓
#define SOLAR_PIN     35
#define SOLAR_R1      10000.0
#define SOLAR_R2      10000.0

// OLED
#define SCREEN_WIDTH  128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// 感測器資料更新間隔 (ms)
#define SENSOR_INTERVAL_MS 10000

// OLED 更新間隔 (ms) - 10 分鐘
#define OLED_UPDATE_MS     120000

// WiFi 檢查間隔 (ms)
#define WIFI_CHECK_MS      20000

// 功率閾值 (mW)
#define POWER_LOW_MAX      200
#define POWER_MEDIUM_MAX   600
// ================================================

// ==================== 全域變數 ====================
// 感測器狀態
bool ina219_ok = false;
bool dht_ok = false;
bool oled_ok = false;
bool ledInitialized = false;

// 最新感測值 (由 sensor 任務更新)
struct SensorData {
  float temperature = 0;
  float humidity = 0;
  float busvoltage = 0;
  float shuntvoltage = 0;
  float loadvoltage = 0;
  float current_mA = 0;
  float power_mW = 0;
  float solarVoltage = 0;
  int ldrValue = 0;
  unsigned long timestamp = 0;  // 秒
};
SensorData sensorData;
SensorData lastDisplayedData;

// LED 動畫
// LED 動畫
Adafruit_NeoPixel pixels(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);
unsigned long lastLedUpdate = 0;

// 時間管理
unsigned long lastSensorRead = 0;
unsigned long lastOledUpdate = 0;
unsigned long lastWifiCheck = 0;
// ================================================

// ==================== 函數宣告 ====================
void initHardware();
void connectWiFi();
void checkWiFi();
void readSensors();
void uploadData();
void updateOLED();
void updateLEDs();
uint32_t Wheel(byte WheelPos);
// ================================================

void setup() {
  Serial.begin(115200);
  initHardware();
  connectWiFi();
}

void loop() {
  unsigned long now = millis();

  // 1. 定期讀取感測器 (10秒)
  if (now - lastSensorRead >= SENSOR_INTERVAL_MS) {
    lastSensorRead = now;
    readSensors();
    uploadData();           // 讀取後立即上傳
  }

  // 2. 定期更新 OLED (10分鐘)
  if (now - lastOledUpdate >= OLED_UPDATE_MS) {
    lastOledUpdate = now;
    updateOLED();
  }

  // 3. 定期檢查 WiFi (20秒)
  if (now - lastWifiCheck >= WIFI_CHECK_MS) {
    lastWifiCheck = now;
    checkWiFi();
  }

  // 4. 定期更新 LED (100ms) - 現在是全亮，但仍定時更新以切換模式
  if (now - lastLedUpdate >= LED_UPDATE_MS) {
    lastLedUpdate = now;
    updateLEDs();
  }

  delay(10);
}

// ==================== 初始化 ====================
void initHardware() {
  Serial.println("\n=== 系統啟動 ===");

  // LED 燈條
  pixels.begin();
  pixels.setBrightness(LED_BRIGHTNESS);
  Serial.println("✅ LED 初始化完成");
  // 開機閃藍燈 3 次
  for (int j = 0; j < 3; j++) {
    for (int i = 0; i < NUM_LEDS; i++) pixels.setPixelColor(i, pixels.Color(0, 0, 255));
    pixels.show();
    delay(200);
    pixels.clear();
    pixels.show();
    delay(200);
  }

  // I2C
  Wire.begin();

  // OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("⚠️ OLED 初始化失敗");
    oled_ok = false;
  } else {
    Serial.println("✅ OLED 初始化成功");
    oled_ok = true;
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.cp437(true);
    display.setCursor(0, 0);
    display.println("系統啟動中...");
    display.display();
  }

  // INA219
  if (!ina219.begin()) {
    Serial.println("⚠️ 找不到 INA219！請檢查接線");
    ina219_ok = false;
  } else {
    Serial.println("✅ INA219 初始化成功");
    ina219.setCalibration_16V_400mA();
    ina219_ok = true;
  }

  // DHT22
  dht.begin();
  delay(2000);  // 等待感測器穩定
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (!isnan(h) && !isnan(t)) {
    Serial.printf("✅ DHT22 讀取成功: %.1f°C, %.1f%%\n", t, h);
    dht_ok = true;
  } else {
    Serial.println("⚠️ DHT22 讀取失敗");
    dht_ok = false;
  }

  // 類比輸入腳位
  pinMode(LDR_PIN, INPUT);
  pinMode(SOLAR_PIN, INPUT);
  Serial.println("✅ 光敏電阻/太陽能板初始化完成");
}

void connectWiFi() {
  Serial.printf("連線到 WiFi: %s\n", ssid);
  WiFi.begin(ssid, password);
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 30) {
    delay(1000);
    Serial.print(".");
    attempts++;
    if (attempts % 5 == 0) {
      for (int i = 0; i < NUM_LEDS; i++) pixels.setPixelColor(i, pixels.Color(255, 255, 0));
      pixels.show();
      delay(100);
      pixels.clear();
      pixels.show();
    }
  }
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\n✅ WiFi 連線成功");
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
    for (int i = 0; i < NUM_LEDS; i++) pixels.setPixelColor(i, pixels.Color(0, 255, 0));
    pixels.show();
    delay(1000);
    pixels.clear();
    pixels.show();
  } else {
    Serial.println("\n⚠️ WiFi 連線失敗，將繼續離線運作");
    for (int i = 0; i < NUM_LEDS; i++) pixels.setPixelColor(i, pixels.Color(255, 0, 0));
    pixels.show();
    delay(1000);
    pixels.clear();
    pixels.show();
  }
}

// ==================== WiFi 維護 ====================
void checkWiFi() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("⚠️ WiFi 斷線，嘗試重新連線...");
    WiFi.reconnect();
    int attempts = 0;
    while (WiFi.status() != WL_CONNECTED && attempts < 20) {
      delay(500);
      Serial.print(".");
      attempts++;
    }
    if (WiFi.status() == WL_CONNECTED) {
      Serial.println("\n✅ WiFi 重新連線成功");
    } else {
      Serial.println("\n❌ WiFi 重新連線失敗");
    }
  }
}

// ==================== 感測器讀取 ====================
void readSensors() {
  Serial.println("\n--- 讀取感測器 ---");

  // INA219
  if (ina219_ok) {
    sensorData.shuntvoltage = ina219.getShuntVoltage_mV();
    sensorData.busvoltage = ina219.getBusVoltage_V();
    sensorData.current_mA = ina219.getCurrent_mA();
    sensorData.power_mW = ina219.getPower_mW();
    sensorData.loadvoltage = sensorData.busvoltage + (sensorData.shuntvoltage / 1000);
  } else {
    sensorData.shuntvoltage = sensorData.busvoltage = sensorData.current_mA = sensorData.power_mW = sensorData.loadvoltage = 0;
  }

  // DHT22
  if (dht_ok) {
    sensorData.humidity = dht.readHumidity();
    sensorData.temperature = dht.readTemperature();
    if (isnan(sensorData.humidity) || isnan(sensorData.temperature)) {
      sensorData.humidity = sensorData.temperature = 0;
    }
  } else {
    sensorData.humidity = sensorData.temperature = 0;
  }

  // 光敏電阻
  sensorData.ldrValue = analogRead(LDR_PIN);

  // 太陽能板電壓
  int solarRaw = analogRead(SOLAR_PIN);
  float voltageAtPin = (solarRaw * 3.3) / 4095.0;
  sensorData.solarVoltage = voltageAtPin * ((SOLAR_R1 + SOLAR_R2) / SOLAR_R2);

  // 時間戳 (秒)
  sensorData.timestamp = millis() / 1000;

  // 列印
  Serial.printf("溫度: %.1f°C, 濕度: %.1f%%, 電流: %.2f mA, 負載電壓: %.2f V, 功率: %.1f mW, 太陽能: %.2f V, 光敏: %d\n",
                sensorData.temperature, sensorData.humidity, sensorData.current_mA,
                sensorData.loadvoltage, sensorData.power_mW, sensorData.solarVoltage, sensorData.ldrValue);
}

// ==================== 資料上傳 ====================
void uploadData() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("⚠️ WiFi 未連線，跳過上傳");
    return;
  }

  HTTPClient http;
  http.begin(serverUrl);
  http.addHeader("Content-Type", "application/json");

  StaticJsonDocument<512> doc;
  doc["device_id"] = "ESP32_01";
  doc["timestamp_esp"] = sensorData.timestamp;
  doc["solar_voltage"] = sensorData.solarVoltage;

  JsonObject power = doc.createNestedObject("power");
  power["bus_voltage"] = sensorData.busvoltage;
  power["shunt_voltage"] = sensorData.shuntvoltage;
  power["load_voltage"] = sensorData.loadvoltage;
  power["current_ma"] = sensorData.current_mA;
  power["power_mw"] = sensorData.power_mW;

  JsonObject env = doc.createNestedObject("environment");
  env["temperature_c"] = sensorData.temperature;
  env["humidity_percent"] = sensorData.humidity;
  env["illuminance_raw"] = sensorData.ldrValue;

  String jsonString;
  serializeJson(doc, jsonString);

  Serial.println("📤 上傳資料...");
  int httpCode = http.POST(jsonString);
  if (httpCode > 0) {
    Serial.printf("✅ 伺服器回應 %d\n", httpCode);
    String response = http.getString();
    Serial.println(response);
  } else {
    Serial.printf("❌ 傳送失敗，錯誤碼: %d\n", httpCode);
  }
  http.end();
}

// ==================== OLED 顯示 ====================
void updateOLED() {

  if (!oled_ok) return;

  // 檢查數值是否有變化
  if (
    sensorData.temperature == lastDisplayedData.temperature &&
    sensorData.humidity == lastDisplayedData.humidity &&
    sensorData.current_mA == lastDisplayedData.current_mA &&
    sensorData.loadvoltage == lastDisplayedData.loadvoltage &&
    sensorData.solarVoltage == lastDisplayedData.solarVoltage
  ) {
    return; // 沒變化就不更新
  }

  display.clearDisplay();

  display.setCursor(0, 0);
  display.print("Temp:");
  display.print(sensorData.temperature, 1);
  display.print("C ");

  display.print("Hum:");
  display.print(sensorData.humidity, 0);
  display.print("%");

  display.setCursor(0, 16);
  display.print("Current:");
  display.print(sensorData.current_mA, 0);
  display.print("mA");

  display.setCursor(0, 32);
  display.print("Voltage:");
  display.print(sensorData.loadvoltage, 2);
  display.print("V");

  display.setCursor(0, 48);
  display.print("Solar:");
  display.print(sensorData.solarVoltage, 1);
  display.print("V ");

  int hrs = sensorData.timestamp / 3600;
  int mins = (sensorData.timestamp % 3600) / 60;

  display.print(hrs);
  display.print("h");
  display.print(mins);
  display.print("m");

  display.display();

  // 保存目前顯示數據
  lastDisplayedData = sensorData;
}

// ==================== LED 控制 ====================
// 修改重點：
// 1. 固定亮度 (使用 LED_BRIGHTNESS = 20)
// 2. 8顆全亮，永遠同一種粉色
// 3. 完全消除顏色變化帶來的耗電差異

void updateLEDs() {

  // 只初始化一次 LED 顏色
  if (!ledInitialized) {

    pixels.setBrightness(LED_BRIGHTNESS);

    // 固定粉紅色 (Hot Pink)
    uint32_t pinkColor = pixels.Color(255, 105, 180);

    for (int i = 0; i < NUM_LEDS; i++) {
      pixels.setPixelColor(i, pinkColor);
    }

    pixels.show();

    ledInitialized = true;
  }
}


uint32_t Wheel(byte WheelPos) {
  if (WheelPos < 85) {
    return pixels.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  } else if (WheelPos < 170) {
    WheelPos -= 85;
    return pixels.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else {
    WheelPos -= 170;
    return pixels.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}