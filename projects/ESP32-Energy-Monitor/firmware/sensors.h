#ifndef SENSORS_H
#define SENSORS_H

#include <Arduino.h>

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
  unsigned long timestamp = 0;
};

extern SensorData sensorData;
extern SensorData lastDisplayedData;

void readSensors();

#endif