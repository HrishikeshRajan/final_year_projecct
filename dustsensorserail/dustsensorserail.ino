#include <SoftwareSerial.h>
#include <Arduino.h>
#include <U8g2lib.h>
#include <SPI.h>
#include <Wire.h>

SoftwareSerial mySerial(8, 7);
U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C u8g2(U8G2_R0); 
int measurePin = A0;
int ledPower = 12;

unsigned int samplingTime = 280;
unsigned int deltaTime = 40;
unsigned int sleepTime = 9680;

float voMeasured = 0;
float calcVoltage = 0;
float dustDensity = 0;

void setup(){
  Serial.begin(9600);
  mySerial.begin(9600)
  u8g2.begin();
  pinMode(ledPower,OUTPUT);
  u8g2.clearBuffer();          // clear the internal memory
   u8g2.setFont(u8g2_font_logisoso24_tr);  // choose a suitable font at https://github.com/olikraus/u8g2/wiki/fntlistall
   u8g2.drawStr(8,29,"Welcome");  // write something to the internal memory
   u8g2.sendBuffer();         // transfer internal memory to the display
   delay(800);

   u8g2.clearBuffer();         // clear the internal memory
   u8g2.setFont(u8g2_font_logisoso24_tr);  // choose a suitable font at https://github.com/olikraus/u8g2/wiki/fntlistall
   u8g2.drawStr(40,26,"TO");  // write something to the internal memory
   (u8g2.sendBuffer();         // transfer internal memory to the display
   delay(800);
   u8g2.clearBuffer();         // clear the internal memory
   u8g2.setFont(u8g2_font_logisoso20_tr);  // choose a suitable font at https://github.com/olikraus/u8g2/wiki/fntlistall
   u8g2.drawStr(16,26,"Maker.Pro");  // write something to the internal memory
   u8g2.sendBuffer()         // transfer internal memory to the display
   delay(2000);
}

void loop(){
  
  
  digitalWrite(ledPower,LOW);
  delayMicroseconds(samplingTime);

  voMeasured = analogRead(measurePin);

  delayMicroseconds(deltaTime);
  digitalWrite(ledPower,HIGH);
  delayMicroseconds(sleepTime);

  calcVoltage = voMeasured*(5.0/1024);
  dustDensity = 0.17*calcVoltage-0.1;

  if ( dustDensity < 0)
  {
    dustDensity = 0.00;
  }

  Serial.println("Raw Signal Value (0-1023):");
  Serial.println(voMeasured);

  Serial.println("Voltage:");
  Serial.println(calcVoltage);

  Serial.println("Dust Density:");
  Serial.println(dustDensity);
   u8g2.clearBuffer();         // clear the internal memory
   u8g2.setFont(u8g2_font_pxplusibmvga9_tr);  // choose a suitable font at https://github.com/olikraus/u8g2/wiki/fntlistall
   u8g2.drawStr(0,15,"Dust Density ");  // write something to the internal memory
   u8g2.setCursor(0, 31);
   u8g2.print(dustDensity); 
  // u8g2.drawStr(0,31,"AHHH123");  // write something to the internal memory
   
//   u8g.print("Hello World!")
   u8g2.sendBuffer();         // transfer internal memory to the display

  delay(1000);
}
