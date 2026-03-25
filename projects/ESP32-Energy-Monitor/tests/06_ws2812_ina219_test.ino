#include <Wire.h>
#include <Adafruit_INA219.h>
#include <Adafruit_NeoPixel.h>

#define PIN 5
#define NUMPIXELS 8

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_RGB + NEO_KHZ800);
Adafruit_INA219 ina219;

void setup() {
  Serial.begin(115200);
  
  pixels.begin();
  pixels.setBrightness(50);
  
  Wire.begin();
  
  if (!ina219.begin()) {
    Serial.println("❌ INA219 失敗");
  } else {
    ina219.setCalibration_16V_400mA();
    Serial.println("✅ INA219 成功");
  }
}

void loop() {
  float power_mW = ina219.getPower_mW();
  
  if (power_mW < 100) {
    for(int i=0; i<NUMPIXELS; i++) pixels.setPixelColor(i, pixels.Color(0, 255, 0));
  } else if (power_mW < 500) {
    for(int i=0; i<NUMPIXELS; i++) pixels.setPixelColor(i, pixels.Color(255, 255, 0));
  } else {
    for(int i=0; i<NUMPIXELS; i++) pixels.setPixelColor(i, pixels.Color(255, 0, 0));
  }
  pixels.show();
  
  Serial.print("功率: "); Serial.print(power_mW); Serial.println(" mW");
  delay(1000);
}