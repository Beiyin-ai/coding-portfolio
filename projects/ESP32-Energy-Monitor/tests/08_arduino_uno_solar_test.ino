const int sensorPin = A0;
float vRef = 5.0;
float resA = 10000.0;
float resB = 10000.0;

void setup() {
  Serial.begin(9600);
  Serial.println("太陽能板測試 (UNO)");
}

void loop() {
  int rawValue = analogRead(sensorPin);
  float vAtPin = (rawValue * vRef) / 1024.0;
  float vSolar = vAtPin * ((resA + resB) / resB);
  
  Serial.print("類比: "); Serial.print(rawValue);
  Serial.print(" | 電壓: "); Serial.print(vSolar);
  Serial.println(" V");
  
  delay(500);
}