#ifndef LED_H
#define LED_H

#include <FastLED.h>
#include "config.h"

class LED {
public:
  void init() {
    FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
    FastLED.setBrightness(LED_BRIGHTNESS);
    currentColor = CRGB::Blue;
  }
  
  void setColor(CRGB color) {
    currentColor = color;
    leds[0] = currentColor;
    FastLED.show();
  }
  
  void setColor(uint8_t r, uint8_t g, uint8_t b) {
    currentColor = CRGB(r, g, b);
    leds[0] = currentColor;
    FastLED.show();
  }
  
  void rainbowEffect() {
    static uint8_t hue = 0;
    leds[0] = CHSV(hue, 255, 255);
    FastLED.show();
    hue += 3;
  }
  
  void playAnimation() {
    for(int i = 0; i < 10; i++) {
      setColor(255, 0, 0);   // Red
      delay(100);
      setColor(0, 255, 0);   // Green
      delay(100);
      setColor(0, 0, 255);   // Blue
      delay(100);
    }
  }
  
  void turnOff() {
    setColor(0, 0, 0);
  }
  
private:
  CRGB leds[NUM_LEDS];
  CRGB currentColor;
};

#endif
