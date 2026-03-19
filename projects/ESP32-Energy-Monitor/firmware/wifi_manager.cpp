#include "wifi_manager.h"
#include "config.h"
#include "hardware.h"

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
    Serial.println("\n⚠️ WiFi 連線失敗");
    for (int i = 0; i < NUM_LEDS; i++) pixels.setPixelColor(i, pixels.Color(255, 0, 0));
    pixels.show();
    delay(1000);
    pixels.clear();
    pixels.show();
  }
}

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