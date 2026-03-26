#ifndef WIFI_MANAGER_H
#define WIFI_MANAGER_H

#include <Arduino.h>
#include <WiFi.h>

extern String serverUrl;  // 宣告全域變數

void connectWiFi();
void checkWiFi();

#endif