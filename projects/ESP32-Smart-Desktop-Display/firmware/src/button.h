#ifndef BUTTON_H
#define BUTTON_H

#include <Arduino.h>
#include "config.h"

class Button {
public:
  void init() {
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    lastState = digitalRead(BUTTON_PIN);
    pressStartTime = 0;
    wasPressedFlag = false;
  }
  
  void update() {
    int currentState = digitalRead(BUTTON_PIN);
    unsigned long currentTime = millis();
    
    // Detect button press (HIGH to LOW)
    if (lastState == HIGH && currentState == LOW) {
      pressStartTime = currentTime;
      Serial.println("Button pressed");
    }
    
    // Detect button release (LOW to HIGH)
    if (lastState == LOW && currentState == HIGH) {
      unsigned long pressDuration = currentTime - pressStartTime;
      
      if (pressDuration > DEBOUNCE_DELAY) {
        wasPressedFlag = true;
        lastPressDuration = pressDuration;
        Serial.print("Button released after ");
        Serial.print(pressDuration);
        Serial.println(" ms");
      }
    }
    
    lastState = currentState;
  }
  
  bool wasPressed() {
    if (wasPressedFlag) {
      wasPressedFlag = false;
      return true;
    }
    return false;
  }
  
  bool isLongPress() {
    return lastPressDuration >= LONG_PRESS_DURATION;
  }
  
  unsigned long getPressDuration() {
    return lastPressDuration;
  }
  
  bool isPressed() {
    return digitalRead(BUTTON_PIN) == LOW;
  }
  
private:
  int lastState;
  unsigned long pressStartTime;
  bool wasPressedFlag;
  unsigned long lastPressDuration;
};

#endif
