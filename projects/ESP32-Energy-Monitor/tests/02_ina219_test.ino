#include <Wire.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 ina219;

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);
  
  Serial.println("INA219 測試開始");
  
  if (!ina219.begin()) {
    Serial.println("❌ 找不到 INA219！檢查接線");
    while (1) delay(10);
  }
  
  ina219.setCalibration_16V_400mA();
  Serial.println("✅ INA219 初始化成功");
}

void loop() {
  float busvoltage = ina219.getBusVoltage_V();
  float current_mA = ina219.getCurrent_mA();
  float power_mW = ina219.getPower_mW();
  
  Serial.print("電壓: "); Serial.print(busvoltage); Serial.print(" V | ");
  Serial.print("電流: "); Serial.print(current_mA); Serial.print(" mA | ");
  Serial.print("功率: "); Serial.print(power_mW); Serial.println(" mW");
  
  delay(1000);
}