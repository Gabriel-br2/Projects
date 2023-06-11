/*
  Program: CollorRGB_HEX
  Author: Gabriel Rocha de Souza
  Version: Portifolio Features 
  Concluded on 07/06/2023
  Brief Description: 
    Collor change by using rgb hexcode   

    Input: a rgb value in hex_code 
*/

#define RED_PIN 22
#define GREEN_PIN 3 
#define BLUE_PIN 21

void changeColor(String hexCode);

struct RGB {
  int red;
  int green;
  int blue;
};

void setup(){
  Serial.begin(9600);

  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT); 
}

void loop(){
  changeColor("E1C043");
}

RGB hexToRGB(const String& hexCode) {
  RGB rgb;
  String sanitizedHex = hexCode;  
  unsigned long hexValue = strtoul(sanitizedHex.c_str(), NULL, 16);
  
  rgb.red = (hexValue >> 16) & 0xFF;
  rgb.green = (hexValue >> 8) & 0xFF;
  rgb.blue = hexValue & 0xFF;
  
  return rgb;
}

void changeColor(String hexCode){
  RGB rgb = hexToRGB(hexCode);
  analogWrite(RED_PIN,  rgb.red);
  analogWrite(GREEN_PIN,rgb.green);
  analogWrite(BLUE_PIN, rgb.blue);
}