#ifndef CONFIG_H
#define CONFIG_H

// DHT sensor type
#define DHTTYPE DHT22

// Hardware pin definitions
#define OLED_SDA_PIN 21
#define OLED_SCL_PIN 22
#define DHT_PIN 4
#define LED_PIN 13
#define BUTTON_PIN 15

// Display settings
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_ADDRESS 0x3C

// LED settings
#define NUM_LEDS 1
#define LED_BRIGHTNESS 100

// Button settings
#define DEBOUNCE_DELAY 50
#define LONG_PRESS_DURATION 2000

// Date settings (for countdown)
#define TARGET_MONTH 1
#define TARGET_DAY 13
#define CURRENT_YEAR 2026
#define CURRENT_MONTH 1
#define CURRENT_DAY 4

// Update intervals (ms)
#define TEMP_UPDATE_INTERVAL 2000
#define DISPLAY_UPDATE_INTERVAL 50
#define MARQUEE_UPDATE_INTERVAL 50

// Marquee messages
const char* MARQUEE_MESSAGES[] = {
  "Birthday in 9 days",
  "IoT Learning Project",
  "ESP32 + OLED + DHT22",
  "Smart Desktop Display"
};

// Love messages (for message mode)
const char* LOVE_MESSAGES[] = {
  "I miss you ��",
  "I love you ❤️",
  "My best gift 🎁",
  "Thank you 🌟",
  "See you soon 🌞",
  "My world 🌈",
  "Hug you 🤗",
  "Can't wait 😊",
  "My everything 💖",
  "Love forever 💘"
};

#endif
