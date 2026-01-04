#ifndef DISPLAY_H
#define DISPLAY_H

#include <U8g2lib.h>

class Display {
public:
  Display(U8G2_SSD1306_128X64_NONAME_F_HW_I2C* display) : u8g2(display) {}
  
  void init() {
    // Display is initialized in main.cpp
  }
  
  void clearScreen() {
    u8g2->clearBuffer();
  }
  
  void showScreen() {
    u8g2->sendBuffer();
  }
  
private:
  U8G2_SSD1306_128X64_NONAME_F_HW_I2C* u8g2;
};

#endif
