const int PIN_LED = 13;
const int LED_INTERVAL = 300;

int led_status = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(PIN_LED, OUTPUT);

  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  int inputchar;
  inputchar = Serial.read();

  if(inputchar!=-1) {
    switch(inputchar){
      case '0':
        led_status = 0;
        break;
      case '1':
        led_status = 1;
        break;
    }    
  }
  
  if(led_status == 1) {
    digitalWrite(PIN_LED, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(LED_INTERVAL);                       // wait for a second
    digitalWrite(PIN_LED, LOW);    // turn the LED off by making the voltage LOW
    delay(LED_INTERVAL);                       // wait for a second
  } else {
    digitalWrite(PIN_LED, LOW);    // turn the LED off by making the voltage LOW
  }
}

