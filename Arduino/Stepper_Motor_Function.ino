/*
  Program: Stepper Motor Function 
  Author: Gabriel Rocha de Souza
  Version: Portifolio Features 
  Concluded on 23/05/2023
  Brief Description: 
    Function to control stepper motor, 
    based on speed and number of revolutions
    
  Parameters
    Speed
      0 to 100 (%)
    
    Distance
      number of laps (negative for couter-clockwise)
*/

int speed;
float distance;
int pins[] = {13,12,14,27};

void StepperMotor_ULN2003(int speed, float distance);

void setup() {
  Serial.begin(9600);  
  for(int i=0 ; i < 4 ; i++){
    pinMode(pins[i],OUTPUT);
  }
}

void loop() {
  if(Serial.available() > 0){  
    speed = Serial.parseInt();
    distance = Serial.parseFloat();

    StepperMotor_ULN2003(speed, distance);
  }
}

void StepperMotor_ULN2003(int speed, float distance){
  int begin = 0, end = 4, add = 1, side = 1;
  const int StepsRevolution_ULN2003 = 512;

  distance = distance*StepsRevolution_ULN2003;

  if(distance < 0){
    begin = 3;end = -1;add = -1;side = -1;    
    distance = distance * -1;
  }
  if(speed > 100){
    speed = 100;
  }

  for (int step_count = 0;step_count <= distance; step_count ++){
    for(int i = begin; (((side == 1) && (i < end)) || ((side == -1) && (i > end))); i=i+add){  
      digitalWrite(pins[i],HIGH); 
      delay(105-speed); 
      digitalWrite(pins[i],LOW);
      delay(2);
    }
  }
}

