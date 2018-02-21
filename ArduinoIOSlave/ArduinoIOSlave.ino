#include <Servo.h> 

//////////
Servo victor1;
Servo victor2;
Servo servo1;
//////////
int victor1pin = 9;
int victor2pin = 10;
int servo1pin = 11;
//////////
int minPulse = 1000;
int maxPulse = 2000;
//////////
int userInput[3];    // raw input from serial buffer, (3 bytes)
int startbyte;       // (1st Byte) start byte, begin reading input
int servo;           // (2nd Byte) which object to update PWM
int pos;             // (3rd Byte) 0-180 PWM Value to update too
int i;               // iterator
//////////
int ledPin = 13;
int pinState = LOW;

void setup() 
{ 
  victor1.attach(victor1pin, minPulse, maxPulse);
  victor2.attach(victor2pin, minPulse, maxPulse);
  servo1.attach(servo1pin, minPulse, maxPulse);
  //////////
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
} 

void loop() 
{ 
  
  if (Serial.available() > 2) {  // wait until 3 bytes min. are in buffer
    startbyte = Serial.read();  // Read the first byte
    if (startbyte == 255) {  // If it's really the startbyte (255) ...
      for (i=0;i<2;i++) {  // ... then get the next two bytes
        userInput[i] = Serial.read();
      }
      servo = userInput[0];  // First byte = servo to move?
      pos = userInput[1];  // Second byte = which position?
      if (pos == 255) { servo = 255; }  // Packet error checking and recovery      
      switch (servo) {  // Assign new position to appropriate servo
        case 1:
          victor1.write(pos); // move victor1 to 'pos'
          break;
        case 2:
          victor2.write(pos);
          break;
        case 3:
          servo1.write(pos);
          break;        
        case 11:  // LED on Pin 13 for digital on/off
          if (pos == 180) {
            if (pinState == LOW) { pinState = HIGH; }
            else { pinState = LOW; }
          }
          if (pos == 0) {
            pinState = LOW;
          }
          digitalWrite(ledPin, pinState);
          break;
      }
    }
  }
}

