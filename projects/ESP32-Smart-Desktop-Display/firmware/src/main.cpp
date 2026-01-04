#include <Arduino.h>
#include <U8g2lib.h>
#include <DHT.h>
#include <FastLED.h>
#include "config.h"
#include "display.h"
#include "sensors.h"
#include "led.h"
#include "button.h"

// Global objects
U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, U8X8_PIN_NONE);
DHT dht(DHT_PIN, DHTTYPE);
LED ledControl;
Button button;
Sensors sensors(&dht);

// Display modes
enum DisplayMode {
  MODE_NORMAL,
  MODE_COUNTER,
  MODE_MESSAGE,
  MODE_SPECIAL
};

DisplayMode currentMode = MODE_NORMAL;

// Variables for display
String marqueeText = MARQUEE_MESSAGES[0];
int marqueePosition = SCREEN_WIDTH;
int messageIndex = 0;
unsigned long lastMessageChange = 0;
unsigned long lastTempUpdate = 0;
float temperature = 0;
float humidity = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("==================================");
  Serial.println("ESP32 Smart Desktop Display");
  Serial.println("Learning Project - IoT Starter");
  Serial.println("==================================");
  
  // Initialize components
  u8g2.begin();
  dht.begin();
  ledControl.init();
  button.init();
  
  // Set initial LED color
  ledControl.setColor(CRGB::Blue);
  
  Serial.println("System initialized successfully");
  Serial.println("Button functions:");
  Serial.println("- Short press: Change display mode");
  Serial.println("- Long press (2s): Special animation");
  Serial.println("Current mode: Normal");
}

void updateMarquee() {
  marqueePosition--;
  int textWidth = marqueeText.length() * 6;
  if (marqueePosition < -textWidth) {
    marqueePosition = SCREEN_WIDTH;
  }
}

void updateTemperature() {
  if (millis() - lastTempUpdate > TEMP_UPDATE_INTERVAL) {
    temperature = dht.readTemperature();
    humidity = dht.readHumidity();
    
    if (!isnan(temperature) && !isnan(humidity)) {
      Serial.printf("Temperature: %.1f°C, Humidity: %.1f%%\n", temperature, humidity);
    } else {
      Serial.println("Failed to read from DHT sensor");
    }
    
    lastTempUpdate = millis();
  }
}

void updateDisplay() {
  u8g2.clearBuffer();
  
  switch (currentMode) {
    case MODE_NORMAL:
      // Header: Date
      u8g2.setFont(u8g2_font_ncenB10_tr);
      u8g2.setCursor(0, 12);
      u8g2.printf("%02d/%02d/%02d", CURRENT_YEAR-2000, CURRENT_MONTH, CURRENT_DAY);
      
      // Days count
      u8g2.setCursor(90, 12);
      u8g2.printf("%d days", TARGET_DAY - CURRENT_DAY);
      
      // Time
      u8g2.setFont(u8g2_font_ncenB14_tr);
      u8g2.setCursor(0, 35);
      u8g2.printf("%02d:%02d", 16, 30);
      
      // Temperature & Humidity
      u8g2.setFont(u8g2_font_ncenB08_tr);
      u8g2.setCursor(0, 50);
      u8g2.printf("T:%.1fC", temperature);
      u8g2.setCursor(64, 50);
      u8g2.printf("H:%.1f%%", humidity);
      
      // Marquee
      u8g2.setCursor(marqueePosition, 62);
      u8g2.print(marqueeText);
      
      // Mode indicator
      u8g2.setCursor(0, 62);
      u8g2.print("N");
      break;
      
    case MODE_COUNTER:
      u8g2.setFont(u8g2_font_ncenB12_tr);
      u8g2.setCursor(20, 15);
      u8g2.print("COUNTDOWN");
      
      u8g2.setFont(u8g2_font_inb33_mn);
      u8g2.setCursor(40, 48);
      u8g2.print(TARGET_DAY - CURRENT_DAY);
      
      u8g2.setFont(u8g2_font_ncenB10_tr);
      u8g2.setCursor(78, 48);
      u8g2.print("DAYS");
      
      u8g2.setFont(u8g2_font_ncenB08_tr);
      u8g2.setCursor(40, 62);
      u8g2.print("JAN 13");
      
      u8g2.setCursor(0, 62);
      u8g2.print("C");
      break;
      
    case MODE_MESSAGE:
      // Auto change message every 8 seconds
      if (millis() - lastMessageChange > 8000) {
        messageIndex = (messageIndex + 1) % (sizeof(LOVE_MESSAGES)/sizeof(LOVE_MESSAGES[0]));
        lastMessageChange = millis();
      }
      
      u8g2.setFont(u8g2_font_ncenB10_tr);
      u8g2.setCursor(40, 12);
      u8g2.print("MESSAGE");
      
      u8g2.setCursor(20, 40);
      u8g2.print(LOVE_MESSAGES[messageIndex]);
      
      u8g2.setFont(u8g2_font_ncenB08_tr);
      u8g2.setCursor(20, 62);
      u8g2.print("Press for next");
      
      u8g2.setCursor(0, 62);
      u8g2.print("L");
      break;
      
    case MODE_SPECIAL:
      static unsigned long lastAnimChange = 0;
      static int animFrame = 0;
      
      if (millis() - lastAnimChange > 3000) {
        animFrame = (animFrame + 1) % 3;
        lastAnimChange = millis();
      }
      
      switch (animFrame) {
        case 0:
          u8g2.setFont(u8g2_font_ncenB12_tr);
          u8g2.setCursor(15, 30);
          u8g2.print("LEARNING");
          u8g2.setCursor(40, 50);
          u8g2.print("PROJECT");
          break;
        case 1:
          u8g2.setFont(u8g2_font_ncenB14_tr);
          u8g2.setCursor(40, 30);
          u8g2.print("ESP32");
          u8g2.setFont(u8g2_font_ncenB08_tr);
          u8g2.setCursor(35, 50);
          u8g2.print("IoT DEVICE");
          break;
        case 2:
          u8g2.setFont(u8g2_font_ncenB12_tr);
          u8g2.setCursor(30, 35);
          u8g2.print("SUCCESS!");
          u8g2.setCursor(45, 55);
          u8g2.print("🎉🚀");
          break;
      }
      
      u8g2.setFont(u8g2_font_ncenB08_tr);
      u8g2.setCursor(0, 62);
      u8g2.print("S");
      break;
  }
  
  u8g2.sendBuffer();
}

void loop() {
  // Update components
  button.update();
  updateTemperature();
  updateMarquee();
  updateDisplay();
  
  // Handle button press
  if (button.wasPressed()) {
    if (button.isLongPress()) {
      // Long press: special animation
      Serial.println("Long press detected - playing animation");
      ledControl.playAnimation();
    } else {
      // Short press: change mode
      currentMode = static_cast<DisplayMode>((currentMode + 1) % 4);
      
      // Update LED color based on mode
      switch (currentMode) {
        case MODE_NORMAL: ledControl.setColor(CRGB::Blue); break;
        case MODE_COUNTER: ledControl.setColor(150, 0, 200); break; // Purple
        case MODE_MESSAGE: ledControl.setColor(255, 50, 150); break; // Pink
        case MODE_SPECIAL: /* Rainbow handled below */ break;
      }
      
      Serial.print("Mode changed to: ");
      switch (currentMode) {
        case MODE_NORMAL: Serial.println("Normal"); break;
        case MODE_COUNTER: Serial.println("Counter"); break;
        case MODE_MESSAGE: Serial.println("Message"); break;
        case MODE_SPECIAL: Serial.println("Special"); break;
      }
    }
  }
  
  // Special mode LED effect
  if (currentMode == MODE_SPECIAL) {
    ledControl.rainbowEffect();
  }
  
  delay(DISPLAY_UPDATE_INTERVAL);
}
