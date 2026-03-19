#include "config.h"
#include "hardware.h"
#include "sensors.h"
#include "wifi_manager.h"
#include "display.h"
#include "led_controller.h"
#include "data_upload.h"

unsigned long lastSensorRead = 0;
unsigned long lastOledUpdate = 0;
unsigned long lastWifiCheck = 0;
unsigned long lastLedUpdate = 0;

void setup() {
  Serial.begin(115200);
  initHardware();
  connectWiFi();
}

void loop() {
  unsigned long now = millis();

  if (now - lastSensorRead >= SENSOR_INTERVAL_MS) {
    lastSensorRead = now;
    readSensors();
    uploadData();
  }

  if (now - lastOledUpdate >= OLED_UPDATE_MS) {
    lastOledUpdate = now;
    updateOLED();
  }

  if (now - lastWifiCheck >= WIFI_CHECK_MS) {
    lastWifiCheck = now;
    checkWiFi();
  }

  if (now - lastLedUpdate >= LED_UPDATE_MS) {
    lastLedUpdate = now;
    updateLEDs();
  }

  delay(10);
}