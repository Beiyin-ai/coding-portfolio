#define LDR_PIN 34

void setup() {
  Serial.begin(115200);
  pinMode(LDR_PIN, INPUT);
  Serial.println("光敏電阻測試開始");
}

void loop() {
  int value = analogRead(LDR_PIN);
  Serial.print("光照值: ");
  Serial.println(value);
  delay(1000);
}