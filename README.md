# A Smarthome project with a Button-device and PC connection

the project: A button device which can send informations with a 433mHz rf-module to a ESP32. This ESP sends commands over the network to a pc where it changes the volume etc. The ESP is an Interface for many other things like a thermostat or anything else. Otherwise the buttons can enable / disable a rgb-strip which is controlled by a self-designed controllrl and they can control wirreles sockets. All these parts have a 3d printed case which gives the whole thing a nice look.


## Items needed:
1. [ESP32](https://www.amazon.de/gp/product/B071P98VTG/ref=ox_sc_act_image_1?smid=A1X7QLRQH87QA3&psc=1) or [ESP8266](https://www.amazon.de/AZDelivery-NodeMCU-ESP8266-ESP-12E-Development/dp/B074Q2WM1Y/ref=sr_1_3?keywords=esp8266&qid=1659355276&s=industrial&sprefix=esp%2Cindustrial%2C109&sr=1-3) for the Network Interface

2. [Attiny84](https://www.reichelt.de/8-bit-attiny-avr-risc-mikrocontroller-8-kb-10-mhz-dip-14-attiny-84v-10-pu-p69889.html?CCOUNTRY=445&LANGUAGE=de&trstct=pos_2&nbc=1&&r=1) for the RGB-strip controller

3. [Attiny85](https://www.reichelt.de/8-bit-attiny-avr-risc-mikrocontroller-8-kb-20-mhz-dip-8-attiny-85-20-pu-p69299.html?&trstct=pos_0&nbc=1) for Thermometer

4. [Thermometer module](https://www.amazon.de/BME280-Feuchte-Temperatur-Atmosph%C3%A4rendruck-Sensor-Modul-mit-IIC-Arduino/dp/B09CYXS3GX/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=arduino+bme280&qid=1659355731&sr=8-4) (which you use doesn't matter)

5. [Buttons](https://www.amazon.de/gp/product/B07Q1BXV7T/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1) for the Buttonmatrix

6. [433 mHz rf-module](https://www.amazon.de/gp/product/B07DJYK29J/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) for the communication between all the devices

7. An antenna to improve the Signal between the rf modules. I used [tinned copper wire](https://www.amazon.de/gp/product/B0043DXICC/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) and I cut it to 17cm. 

8. [Mosfets](https://www.amazon.de/BOJACK-IRFZ44N-IRFZ44NPBF-Gleichrichter-Transistoren/dp/B0831NZHNW/ref=sr_1_7?keywords=irlz44n&qid=1659356180&sprefix=irl%2Caps%2C133&sr=8-7) to controll the RGB-Strip

9. A 10k pulldown resistor ensures shutoff if gate floats.

10. [wireless socket](https://www.amazon.de/Brennenstuhl-Comfort-Line-Funksteckdosen-Set-Funkschalt-Set-Ber%C3%BChrungsschutz/dp/B099653MQ4/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3G57BLJFAH9L8&keywords=funksteckdose&qid=1659357393&sprefix=funksteckdose%2Caps%2C183&sr=8-5) like this, it should have a 433 mHz receiver

11. [Attiny Programmer](https://www.amazon.de/ISP-Programmer-Adapter-STK500-ATmega-ATtiny/dp/B00IYNAXUC/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2QPKQTL35M0SM&keywords=attiny+programmer&qid=1659366848&sprefix=attiny+programme%2Caps%2C140&sr=8-4) (actually unnecessary, I use a Arduino as ISP)

12. 3D Printer (I use a [Ender 3](https://www.amazon.de/Creality-Ender-Resume-Printing-Source/dp/B07JC93LKS/ref=sr_1_5?keywords=ender+3&qid=1659374822&sr=8-5))


## How to Programm a Attiny with the Arduino

1. past "https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json" to Additional Board Managers URLs
2. Select Tools --> Board --> Boards Manager and install Attiny package by David. A Mellis
3. Upload File --> Example --> ArduinoISP to Arduino
4. 10µF capacitor between GND and RESET on the Arduino   
5. connect the following pins from the arduino to one of the attinys (I soldered a shield for the arduino uno because it's not always that complicated) 

 
 | Arduino            | Attiny84 | Attiny85| 
 | -------------------|----------|---------|
 | 5V                 | Pin 1    | Pin 8   |   
 | Pin 10  (RESET)    | Pin 4    | Pin 1   |
 | Pin 11  (MOSI)     | Pin 7    | Pin 5   |
 | Pin 12  (MISO)     | Pin 8    | Pin 6   |    ![85](https://user-images.githubusercontent.com/61635769/182199570-e94b87a4-6133-40f2-8af1-4a560d968bce.png)
 | Pin 13  (SCK)      | Pin 9    | Pin 7   |
 |                    |![84](https://user-images.githubusercontent.com/61635769/182199557-12fc47d7-49d0-46ef-a550-450a76571ac4.png)  | ![85](https://user-images.githubusercontent.com/61635769/182199570-e94b87a4-6133-40f2-8af1-4a560d968bce.png)
 
 optional on the Arduino can you add a few LEDs
 |information  | Pin   |
 |-------------|-------|
 | Heatbeat    | Pin 9 |
 | Error       | Pin 8 |
 | Programming | Pin 7 |
 

 6. select Tools --> Processor --> Attiny84/Attiny85 | Tools --> Clock --> Internal 8MHz | Tools --> Programmer --> Arduino as ISP
 7. and finally Tools --> Burn Bootloader
 now you can upload any programm to the Attiny

 
