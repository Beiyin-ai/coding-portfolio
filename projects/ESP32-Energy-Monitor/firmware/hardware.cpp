#include "hardware.h"
#include "config.h"

Adafruit_INA219 ina219;
DHT dht(DHTPIN, DHTTYPE);
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
Adafruit_NeoPixel pixels(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

bool ina219_ok = false;
bool dht_ok = false;
bool oled_ok = false;

void initHardware() {
  Serial.println("\n=== 系統啟動 ===");

  pixels.begin();
  pixels.setBrightness(LED_BRIGHTNESS);
  Serial.println("✅ LED 初始化完成");
  
  for (int j = 0; j < 3; j++) {
    for (int i = 0; i < NUM_LEDS; i++) pixels.setPixelColor(i, pixels.Color(0, 0, 255));
    pixels.show();
    delay(200);
    pixels.clear();
    pixels.show();
    delay(200);
  }

  Wire.begin();

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

  if (!ina219.begin()) {
    Serial.println("⚠️ 找不到 INA219！");
    ina219_ok = false;
  } else {
    Serial.println("✅ INA219 初始化成功");
    ina219.setCalibration_16V_400mA();
    ina219_ok = true;
  }

  dht.begin();
  delay(2000);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (!isnan(h) && !isnan(t)) {
    Serial.printf("✅ DHT22 成功: %.1f°C, %.1f%%\n", t, h);
    dht_ok = true;
  } else {
    Serial.println("⚠️ DHT22 讀取失敗");
    dht_ok = false;
  }

  pinMode(LDR_PIN, INPUT);
  pinMode(SOLAR_PIN, INPUT);
  Serial.println("✅ 類比輸入初始化完成");
}