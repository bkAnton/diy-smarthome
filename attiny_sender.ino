#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();
void setup() {
  mySwitch.enableTransmit(5);
}
void loop() {
  for (int i = 1; i < 9999; ++i)  {
    mySwitch.send(i, 24);
    delay(5000);
  }
} 
