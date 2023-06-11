/*
  Program: Buzzer Calibrator  
  Author: Gabriel Rocha de Souza
  Version: Portifolio Features 
  Concluded on 11/03/2023
  Brief Description: 
    script to calibrete a buzzer    
*/

#define Buzzer 10
#define Button 9

int frequency = 0;
bool ButonState = 0;

void setup() {
  Serial.begin(9600);
  pinMode(Buzzer,OUTPUT);
  pinMode(Button,INPUT_PULLUP);
}

void loop() {

  if(Serial.available()>0){
    frequency = Serial.parseInt(); 
  }

  Serial.println(frequency);

  ButonState = !digitalRead(Button);

  if(ButonState){tone(Buzzer,frequency);}
  else{noTone(Buzzer);}
}
