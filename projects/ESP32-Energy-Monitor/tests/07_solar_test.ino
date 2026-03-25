#define SOLAR_PIN 35
#define SOLAR_R1 10000.0
#define SOLAR_R2 10000.0

void setup() {
  Serial.begin(115200);
  pinMode(SOLAR_PIN, INPUT);
  Serial.println("太陽能板測試開始");
}

void loop() {
  int raw = analogRead(SOLAR_PIN);
  float vPin = (raw * 3.3) / 4095.0;
  float vSolar = vPin * ((SOLAR_R1 + SOLAR_R2) / SOLAR_R2);
  
  Serial.print("類比: "); Serial.print(raw);
  Serial.print(" | 電壓: "); Serial.print(vSolar);
  Serial.println(" V");
  
  delay(1000);
}