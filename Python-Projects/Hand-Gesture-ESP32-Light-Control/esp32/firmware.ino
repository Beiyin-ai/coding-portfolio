// Hand Gesture Light Control - ESP32 Firmware
// 接收 Jetson Nano 的手勢代碼，控制 WS2812 燈條
// 
// 接線:
// - RX: GPIO 16 (接收 Jetson Nano 資料)
// - TX: GPIO 17 (可選，用於除錯)
// - LED Data: GPIO 33 (連接 WS2812)
//
// 手勢代碼:
// 1 -> Paper   -> 白色
// 2 -> Rock    -> 綠色
// 3 -> Scissors-> 紅色
// 4 -> Unknown -> 熄滅

#include <Adafruit_NeoPixel.h>

// LED 設定
#define LED_PIN     33
#define LED_COUNT   8
#define BRIGHTNESS  100

// 初始化 NeoPixel 物件
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

// 顏色定義
uint32_t color_paper   = strip.Color(255, 255, 255);  // 白色
uint32_t color_rock    = strip.Color(51, 255, 51);    // 綠色 (#33ff33)
uint32_t color_scissors = strip.Color(255, 0, 0);     // 紅色 (#ff0000)
uint32_t color_off     = strip.Color(0, 0, 0);        // 黑色/熄滅

void setup() {
  // 初始化序列通訊
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 16, 17);  // RX=16, TX=17
  
  Serial.println("ESP32 Hand Gesture Light Control");
  Serial.println("等待 Jetson Nano 指令...");
  
  // 初始化 LED 燈條
  strip.begin();
  strip.show();
  strip.setBrightness(BRIGHTNESS);
  
  // 初始顯示彩虹效果
  rainbowCycle(10);
  clearLEDs();
}

void loop() {
  // 檢查序列埠是否有資料
  if (Serial2.available() > 0) {
    char gesture_code = Serial2.read();
    
    // 忽略換行符號
    if (gesture_code == '\n' || gesture_code == '\r') {
      return;
    }
    
    Serial.print("收到手勢代碼: ");
    Serial.println(gesture_code);
    
    // 根據代碼控制 LED
    switch(gesture_code) {
      case '1':  // Paper - 白色
        Serial.println("手勢: 布 -> 白色燈光");
        setAllLEDs(color_paper);
        break;
        
      case '2':  // Rock - 綠色
        Serial.println("手勢: 石頭 -> 綠色燈光");
        setAllLEDs(color_rock);
        break;
        
      case '3':  // Scissors - 紅色
        Serial.println("手勢: 剪刀 -> 紅色燈光");
        setAllLEDs(color_scissors);
        break;
        
      case '4':  // Unknown - 熄滅
        Serial.println("手勢: 未知 -> 熄滅");
        clearLEDs();
        break;
        
      default:
        Serial.println("未知代碼");
        break;
    }
  }
}

// 設定所有 LED 為相同顏色
void setAllLEDs(uint32_t color) {
  for(int i = 0; i < LED_COUNT; i++) {
    strip.setPixelColor(i, color);
  }
  strip.show();
}

// 清除所有 LED
void clearLEDs() {
  setAllLEDs(color_off);
}

// 彩虹效果 (初始化用)
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;
  
  for(j = 0; j < 256; j++) {
    for(i = 0; i < LED_COUNT; i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / LED_COUNT) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// 彩虹顏色輪
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}
