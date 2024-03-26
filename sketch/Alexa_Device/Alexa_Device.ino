/*
 * Project: Alexa Device
 * Description: Portifolio Features
      A exemple of IOT to 
      use with Alexa voice assistent
      
 * Creation date: 30/07/2023
 * Author: Gabriel, GRS
 * GitHub: Gabriel-br2
 * License: GPL-3.0
 */

#include <WiFiManager.h> 
#include <WiFi.h>
#include <Espalexa.h>

#define BUTTON_PINr 5
#define LED_BUTTONr 16 
#define teste 23

// configs
const int n = 6;
int count_buttonR_pressed = 0;

// variable to handle function
bool res;
float timeVec[n];
bool last_buttonR_state = true;
int state = 0;

//main object
WiFiManager wm;
Espalexa espalexa;

//function
void checkButton(int n, float time);
void test_handle(uint8_t brightness);

void setup() {
  Serial.begin(115200);    
  
  pinMode(BUTTON_PINr, INPUT_PULLUP);
  pinMode(LED_BUTTONr, OUTPUT);
  pinMode(teste, OUTPUT);

  digitalWrite(LED_BUTTONr, HIGH);

  wm.setClass("invert");
  res = wm.autoConnect("IOT_WifiConfig");

  if(!res){
    Serial.println("Failed to connect, reseting");
    ESP.restart();
  }
  
  Serial.println("Connected to wifi");
  delay(150);

  //connect to wi-fi
  WiFi.begin();
  unsigned long begin_Time = millis();
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    if ((millis() - begin_Time) > 30000){
      Serial.println("Fail to connect, reseting");
      wm.resetSettings();
      ESP.restart();
    }
  }

  //hold for ip adress
  Serial.println("hold for IP");
  IPAddress localIP = WiFi.localIP();
  while (localIP == IPAddress(0,0,0,0)){
    Serial.print(".");
    localIP = WiFi.localIP();
    delay(150);
  }
  Serial.print("\nConectado IP: ");
  Serial.println(WiFi.localIP());
  
  espalexa.addDevice("Dispositivo", test_handle); 
  espalexa.begin();
  
  digitalWrite(LED_BUTTONr, LOW);
}

void loop() {
  // reconect wi-fi in case of disconnect 
  if (WiFi.status() != WL_CONNECTED){
    Serial.println("lose connect, trying reconect");
    WiFi.begin();
    while(WiFi.status() != WL_CONNECTED){
      checkButton(15);
      Serial.print(".");
      delay(500);
    }
    Serial.println("\nReconnected");
  }

  espalexa.loop();  
  checkButton(15);
}

void test_handle(uint8_t brightness){
  state = !state;
  digitalWrite(teste, state);
  }