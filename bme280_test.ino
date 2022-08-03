#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme;

void setup() {
  Serial.begin(9600);


  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}

void loop() {

  double temp = bme.readTemperature();
  double pressure = bme.readPressure();
  double humidity = bme.readHumidity();
  
  Serial.print("Temperature = ");
  Serial.print(temp);
  Serial.println("*C");

  Serial.print("Pressure = ");
  Serial.print(pressure / 100.0F);
  Serial.println("hPa");

  //Serial.print("Approx. Altitude = ");
  //Serial.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
  //Serial.println("m");

  Serial.print("Humidity = ");
  Serial.print(humidity);
  Serial.println("%");

  Serial.println();
  delay(1000);
}
