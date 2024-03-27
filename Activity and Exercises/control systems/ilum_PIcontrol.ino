#define PIN_Ldr A0
#define PIN_Pot A1 
#define PIN_Lamp 11 

float leitura_pot;
float leitura_ldr;
float maped_leitura_pot;
float maped_leitura_ldr;

float degrau = 0;

float ti = 0;
float ts = 0;

float kp = 0.08;  
float ki = 1.12;

float E;
float P = 0;
float I = 0;

float Controle;
float Saida;

void setup(){
  Serial.begin(2400);
  pinMode(PIN_Pot, INPUT);
  pinMode(PIN_Ldr, INPUT);
  pinMode(PIN_Lamp,OUTPUT);
}

void loop(){
  // degrau aplicado em 8000s
  if (millis() > 4000 && millis() < 8000){
    degrau = 63;
  }
  if (millis() > 8000){
    degrau = 127;
  }

  leitura_pot = analogRead(PIN_Pot);
  maped_leitura_pot = map(leitura_pot,0, 1023, 0, 255);

  leitura_ldr = analogRead(PIN_Ldr);
  maped_leitura_ldr = map(leitura_ldr,0, 1023, 0, 255);

  E = (degrau - maped_leitura_ldr);
  //E = (maped_leitura_pot - maped_leitura_ldr);
  
  P = kp*E;

  ts = (millis() - ti)/1000;
  ti = millis();

  I = I + (ki*ts*E);

  Saida = P + I;

  if(Saida<0) Saida=0;

  Controle = constrain(Saida, 0, 254);
  
  analogWrite(PIN_Lamp, Controle);

 // Serial.print(maped_leitura_pot);
  Serial.print(degrau); 
  Serial.print(" ");
  Serial.println(maped_leitura_ldr);
}