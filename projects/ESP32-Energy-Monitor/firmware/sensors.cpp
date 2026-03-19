#include "sensors.h"
#include "hardware.h"
#include "config.h"

SensorData sensorData;
SensorData lastDisplayedData;

void readSensors() {
  Serial.println("\n--- 讀取感測器 ---");

  if (ina219_ok) {
    sensorData.shuntvoltage = ina219.getShuntVoltage_mV();
    sensorData.busvoltage = ina219.getBusVoltage_V();
    sensorData.current_mA = ina219.getCurrent_mA();
    sensorData.power_mW = ina219.getPower_mW();
    sensorData.loadvoltage = sensorData.busvoltage + (sensorData.shuntvoltage / 1000);
  } else {
    sensorData.shuntvoltage = sensorData.busvoltage = sensorData.current_mA = sensorData.power_mW = sensorData.loadvoltage = 0;
  }

  if (dht_ok) {
    sensorData.humidity = dht.readHumidity();
    sensorData.temperature = dht.readTemperature();
    if (isnan(sensorData.humidity) || isnan(sensorData.temperature)) {
      sensorData.humidity = sensorData.temperature = 0;
    }
  } else {
    sensorData.humidity = sensorData.temperature = 0;
  }

  sensorData.ldrValue = analogRead(LDR_PIN);

  int solarRaw = analogRead(SOLAR_PIN);
  float voltageAtPin = (solarRaw * 3.3) / 4095.0;
  sensorData.solarVoltage = voltageAtPin * ((SOLAR_R1 + SOLAR_R2) / SOLAR_R2);

  sensorData.timestamp = millis() / 1000;

  Serial.printf("溫度: %.1f°C, 濕度: %.1f%%, 電流: %.2f mA, 負載電壓: %.2f V, 功率: %.1f mW, 太陽能: %.2f V, 光敏: %d\n",
                sensorData.temperature, sensorData.humidity, sensorData.current_mA,
                sensorData.loadvoltage, sensorData.power_mW, sensorData.solarVoltage, sensorData.ldrValue);
}