/*
  Program: turning on led by button 
  git-hub: Gabriel-br2
  Author: Gabriel Rocha de Souza
  Version: Portifolio Features 
  Concluded on 08/03/2023
  Brief Description: 
    script to 
    turn on a led by button
*/

#define pushbutton 2
#define led 13

bool ledstate = 0;

void setup(){
  pinMode(pushbutton, INPUT_PULLUP);
  pinMode(led, OUTPUT);
}

void loop(){
  if(digitalRead(pushbutton)== LOW){
    ledstate = 1;
  }
  
  else{
    ledstate = 0;
  }

  digitalWrite(led,ledstate);
  delay(100);
  
}