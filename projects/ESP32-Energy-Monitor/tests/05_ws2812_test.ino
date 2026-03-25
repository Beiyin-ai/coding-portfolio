#include <Adafruit_NeoPixel.h>

#define PIN 5
#define NUMPIXELS 8

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_RGB + NEO_KHZ800);

void setup() {
  pixels.begin();
  pixels.setBrightness(50);
}

void loop() {
  // 紅色
  for(int i=0; i<NUMPIXELS; i++) pixels.setPixelColor(i, pixels.Color(255, 0, 0));
  pixels.show();
  delay(500);
  
  // 綠色
  for(int i=0; i<NUMPIXELS; i++) pixels.setPixelColor(i, pixels.Color(0, 255, 0));
  pixels.show();
  delay(500);
  
  // 藍色
  for(int i=0; i<NUMPIXELS; i++) pixels.setPixelColor(i, pixels.Color(0, 0, 255));
  pixels.show();
  delay(500);
}