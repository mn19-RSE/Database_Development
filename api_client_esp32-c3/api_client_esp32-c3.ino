#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "unslow";
const char* password = "1227Philly!";

const char* server = "http://192.168.0.148:8080/value?ch=humidity";

const int buttonPin = 2;

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);

  WiFi.begin(ssid, password);
  Serial.print("Connecting");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
}

void loop() {
  static bool lastState = HIGH;
  bool state = digitalRead(buttonPin);

  // Detect button press
  if (lastState == HIGH && state == LOW) {
    Serial.println("Button pressed");

    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(server);

      int code = http.GET();
      Serial.print("HTTP code: ");
      Serial.println(code);

      if (code > 0) {
        String payload = http.getString();
        Serial.print("Received value: ");
        Serial.println(payload);
      } else {
        Serial.print("HTTP error: ");
        Serial.println(http.errorToString(code));
      }


      http.end();
    }
  }

  lastState = state;
  delay(50);
}
