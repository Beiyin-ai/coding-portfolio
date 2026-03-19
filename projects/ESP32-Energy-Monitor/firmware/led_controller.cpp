#include "led_controller.h"
#include "config.h"
#include "hardware.h"

#define PINK_R 255
#define PINK_G 105
#define PINK_B 180

void updateLEDs() {
  pixels.setBrightness(LED_BRIGHTNESS);
  
  for (int i = 0; i < NUM_LEDS; i++) {
    pixels.setPixelColor(i, pixels.Color(PINK_R, PINK_G, PINK_B));
  }
  
  pixels.show();
}