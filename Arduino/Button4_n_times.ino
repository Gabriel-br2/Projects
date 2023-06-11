/*
  Program: Button 4 n times
  Author: Gabriel Rocha de Souza
  Version: Portifolio Features 
  Concluded on 07/06/2023
  Brief Description: 
    Execute a specified function when button is 
    pressed n times in x seconds, and turn on a led
    to indicate "button pressed"

    Input: n buttons presssed, x seconds
*/

//reajust para n times

#define BUTTON_PIN 5
#define LED_BUTTON 4 

float timeVec[6] = {0,0,0,0,0,0};
int count_button_pressed = 0;
bool last_state = true;

void checkButton(int n, float time);

void setup(){
  Serial.begin(9600);

  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_BUTTON, OUTPUT); 
}

void loop(){
  checkButton(6, 15);
}

bool allzero(int n, float vetor[]) {
  for (int i = 0; i < n; i++) {
    if (vetor[i] != 0) {
      return true;
    }
  }
  return false;
}

void realignVec(int n, float* vec){
  if (vec[0] != 0){
    return;
  }
 
  else{
    for(int i = 0;i < (n-1);i++){
      vec[i] = vec[i+1]; 
    }
    vec[n-1] = 0;
    realignVec(n, vec);
  }
}

void checkButton(int n, float time){
  if (digitalRead(BUTTON_PIN) == LOW && last_state){
    last_state = false;
    digitalWrite(LED_BUTTON, HIGH);

    for(int j = 0; j < (n-1); j++){  
      if (millis() - timeVec[j] >= (time*1000) && timeVec[j] != 0){
        timeVec[j] = 0;
        count_button_pressed--;
      }
    }

    if (allzero(n,timeVec)){
      realignVec(n,timeVec);
    }

    timeVec[count_button_pressed] = millis();  
    count_button_pressed++;
    
    if (count_button_pressed >= n){
      Serial.println("Function");
      count_button_pressed = 0;
      for (int k = 0; k < n; k++){
        timeVec[k] = 0;
      }
    }
    delay(500);
  }

  else if (digitalRead(BUTTON_PIN) == HIGH){
    digitalWrite(LED_BUTTON, LOW);
    last_state = true;
  }
}