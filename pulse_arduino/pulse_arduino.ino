void setup() {
  // initialize digital pin LED_BUILTIN as an output
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(13,OUTPUT);
}

void loop() {
 digitalWrite(LED_BUILTIN, HIGH); // turn the LED on (HIGH is the voltage level)
                      // wait for a second
 digitalWrite(13, LOW);
 delay(900);
 digitalWrite(LED_BUILTIN, LOW);
 digitalWrite(13,HIGH);
 delay(100);
}
