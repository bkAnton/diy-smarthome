#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();
int lastvalue = 0;

void setup() {
  Serial.begin(9600);
  mySwitch.enableReceive(0); 
}

void loop() {
  if (mySwitch.available()) {
    int value = mySwitch.getReceivedValue();

    if(lastvalue != value)  {   
      Serial.println(value);
    } 
    lastvalue = value;
    
   }
  mySwitch.resetAvailable(); // Hier wird der Empfänger "resettet"
  }
