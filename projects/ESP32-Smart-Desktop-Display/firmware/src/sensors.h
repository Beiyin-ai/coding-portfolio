#ifndef SENSORS_H
#define SENSORS_H

#include <DHT.h>

class Sensors {
public:
  Sensors(DHT* dhtSensor) : dht(dhtSensor) {}
  
  void init() {
    // DHT is initialized in main.cpp
    lastTemperature = 0;
    lastHumidity = 0;
    lastReadTime = 0;
  }
  
  float readTemperature() {
    updateReadings();
    return lastTemperature;
  }
  
  float readHumidity() {
    updateReadings();
    return lastHumidity;
  }
  
  bool isDataValid() {
    return !isnan(lastTemperature) && !isnan(lastHumidity);
  }
  
private:
  DHT* dht;
  float lastTemperature;
  float lastHumidity;
  unsigned long lastReadTime;
  
  void updateReadings() {
    unsigned long currentTime = millis();
    
    // Update every 2 seconds
    if (currentTime - lastReadTime > 2000) {
      float temp = dht->readTemperature();
      float hum = dht->readHumidity();
      
      if (!isnan(temp) && !isnan(hum)) {
        lastTemperature = temp;
        lastHumidity = hum;
      }
      
      lastReadTime = currentTime;
    }
  }
};

#endif
