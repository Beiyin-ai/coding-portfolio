#include "display.h"
#include "hardware.h"
#include "sensors.h"

void updateOLED() {
  if (!oled_ok) return;

  if (sensorData.temperature == lastDisplayedData.temperature &&
      sensorData.humidity == lastDisplayedData.humidity &&
      sensorData.current_mA == lastDisplayedData.current_mA &&
      sensorData.loadvoltage == lastDisplayedData.loadvoltage &&
      sensorData.solarVoltage == lastDisplayedData.solarVoltage) {
    return;
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
  lastDisplayedData = sensorData;
}