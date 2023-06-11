/*
  Program: Servo to position 0 
  git-hub: Gabriel-br2
  Author: Gabriel Rocha de Souza
  Version: Portifolio Features 
  Concluded on 08/03/2023
  Brief Description: 
    script to control servo motor, 
    takes the motor to initial position 0
*/

#include <Servo.h> 

Servo servo_motor;  

void setup() {
  servo_motor.attach(9);  
  servo_motor.write(10); 
}

void loop() {
}