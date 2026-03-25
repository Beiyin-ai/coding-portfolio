#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  Serial.begin(115200);
  Serial.println("OLED 測試開始");
  
  Wire.begin();
  
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("❌ 找不到 OLED！");
    while (1);
  }
  
  Serial.println("✅ 找到 OLED！");
  
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("OLED OK");
  
  display.setTextSize(1);
  display.setCursor(0, 30);
  display.println("SCL:GPIO22");
  display.setCursor(0, 40);
  display.println("SDA:GPIO21");
  display.display();
}

void loop() {
  delay(1000);
}