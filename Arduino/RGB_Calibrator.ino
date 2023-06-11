/*
  Program: RGB calibrator
  Author: Gabriel Rocha de Souza
  Version: Portifolio Features 
  Concluded on 05/06/2023
  Brief Description: 
    Function to control to 
    calibrated a Rgb led
*/

#define BUTTON_PIN 5 
#define RED_PIN 22
#define GREEN_PIN 3 
#define BLUE_PIN 21
#define POT 36 //vp

struct RGB{
  int red;
  int green;
  int blue;
};

bool last = true;
int valueToChange = 0;
int value = 255;
RGB rgb;

void setup(){
  Serial.begin(9600);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(POT, INPUT);

  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
}

void loop(){
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n'); 
    int numbers[3];
    int index = 0;
    char* ptr = strtok(const_cast<char*>(input.c_str()), " ");
    while (ptr != NULL && index < 3) {
      numbers[index] = atoi(ptr);
      ptr = strtok(NULL, " ");
      index++;
    }
    rgb.red = numbers[0];
    rgb.green = numbers[1];
    rgb.blue = numbers[2];

    switch (valueToChange){
    case 0:
      value = numbers[0];
      break;
    case 1:
      value = numbers[1];
      break;
    case 2:
      value = numbers[2];
      break;
  }
  }

  if (digitalRead(BUTTON_PIN) == LOW && last){
    last = false;
    valueToChange++;
    if (valueToChange == 3){
      valueToChange = 0;
    }
  }
  else if (digitalRead(BUTTON_PIN) == HIGH){
    last = true;
  }

  value = map(analogRead(POT),0,4095,0,255);
  delay(250);

  switch (valueToChange){
    case 0:
      rgb.red = value;
      break;
    case 1:
      rgb.green = value;
      break;
    case 2:
      rgb.blue = value;
      break;
  }

  analogWrite(RED_PIN, rgb.red);
  analogWrite(GREEN_PIN, rgb.green);
  analogWrite(BLUE_PIN, rgb.blue);

  Serial.println("");
  Serial.print("R: ");
  Serial.print(rgb.red);
  Serial.print(" | G: ");
  Serial.print(rgb.green);
  Serial.print(" | B: ");
  Serial.print(rgb.blue);
  Serial.print(" | Ch: ");
  Serial.print(valueToChange);

}