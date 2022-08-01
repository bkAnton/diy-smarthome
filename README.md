# A Smarthome project with a Button-device and PC connection

the project: A button device which can send informations with a 433mHz rf-module to a ESP32. This ESP sends commands over the network to a pc where it changes the volume etc. The ESP is an Interface for many other things like a thermostat or anything else. Otherwise the buttons can enable / disable a rgb-strip which is controlled by a self-designed controllrl and they can control wirreles sockets. All these parts have a 3d printed case which gives the whole thing a nice look.


## Items needed:
1.[ESP32](https://www.amazon.de/gp/product/B071P98VTG/ref=ox_sc_act_image_1?smid=A1X7QLRQH87QA3&psc=1) or [ESP8266](https://www.amazon.de/AZDelivery-NodeMCU-ESP8266-ESP-12E-Development/dp/B074Q2WM1Y/ref=sr_1_3?keywords=esp8266&qid=1659355276&s=industrial&sprefix=esp%2Cindustrial%2C109&sr=1-3) for the Network Interface

2.[Attiny84](https://www.reichelt.de/8-bit-attiny-avr-risc-mikrocontroller-8-kb-10-mhz-dip-14-attiny-84v-10-pu-p69889.html?CCOUNTRY=445&LANGUAGE=de&trstct=pos_2&nbc=1&&r=1) for the RGB-strip controller

3.[Attiny85](https://www.reichelt.de/8-bit-attiny-avr-risc-mikrocontroller-8-kb-20-mhz-dip-8-attiny-85-20-pu-p69299.html?&trstct=pos_0&nbc=1) for Thermometer

4.[Thermometer module](https://www.amazon.de/BME280-Feuchte-Temperatur-Atmosph%C3%A4rendruck-Sensor-Modul-mit-IIC-Arduino/dp/B09CYXS3GX/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=arduino+bme280&qid=1659355731&sr=8-4) (which you use doesn't matter)

5.[Buttons](https://www.amazon.de/gp/product/B07Q1BXV7T/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1) for the Buttonmatrix

6.[433 mHz rf-module](https://www.amazon.de/gp/product/B07DJYK29J/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) for the communication between all the devices

7.An antenna to improve the Signal between the rf modules. I used this [tinned copper wire](https://www.amazon.de/gp/product/B0043DXICC/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) and I cut it to 17cm. 

8.[Mosfets](https://www.amazon.de/BOJACK-IRFZ44N-IRFZ44NPBF-Gleichrichter-Transistoren/dp/B0831NZHNW/ref=sr_1_7?keywords=irlz44n&qid=1659356180&sprefix=irl%2Caps%2C133&sr=8-7) to controll the RGB-Strip

9. A 10k pulldown resistor ensures shutoff if gate floats.

10.[wireless socket](https://www.amazon.de/Brennenstuhl-Comfort-Line-Funksteckdosen-Set-Funkschalt-Set-Ber%C3%BChrungsschutz/dp/B099653MQ4/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3G57BLJFAH9L8&keywords=funksteckdose&qid=1659357393&sprefix=funksteckdose%2Caps%2C183&sr=8-5) like this, it should have a 433 mHz receiver


