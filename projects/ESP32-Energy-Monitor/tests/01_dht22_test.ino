#include "DHT.h"

#define DHTPIN 27
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  Serial.println("DHT22 測試開始");
  dht.begin();
}

void loop() {
  delay(2000);
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
  if (isnan(h) || isnan(t)) {
    Serial.println("❌ 讀取失敗，請檢查接線");
    return;
  }
  
  Serial.print("溫度: "); Serial.print(t); Serial.print(" °C, ");
  Serial.print("濕度: "); Serial.print(h); Serial.println(" %");
}