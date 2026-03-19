#include "data_upload.h"
#include "config.h"
#include "sensors.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

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
    if (httpCode == 200) {
      String response = http.getString();
      Serial.println(response);
    }
  } else {
    Serial.printf("❌ 傳送失敗，錯誤碼: %d\n", httpCode);
  }
  
  http.end();
}