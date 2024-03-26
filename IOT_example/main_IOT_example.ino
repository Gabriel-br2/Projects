/*
 * Project: Exemple of IOT device
 * Description: Trab AIC
      A exemple of IOT device with the following features:
      wifi config, wifi reset, button for reset, OTA, Serial->wifi
      
 * Creation date: 30/07/2023
 * Author: Gabriel, GRS
 * GitHub: Gabriel-br2
 * License: GPL-3.0
 */

#include <WiFiManager.h> 
#include <WiFi.h>
#include <WiFiClient.h>
#include <ESPAsyncWebServer.h>
#include <ESPmDNS.h>
#include <Update.h>

#define BUTTON_PINr 5
#define LED_BUTTONr 16 

// configs
const int n = 6;
int count_buttonR_pressed = 0;
String host =      "esp32";
String User =      "admin";
String Password =  "admin";

//Names for Project
String Proj_Name = "Proj Name";
String Autores =   "GRS";
String Version =   "0";
String data =      "05:06:2023";

// variable to handle function
bool res;
float timeVec[n];
volatile bool buttonLock = false;
volatile bool lastStateButton = true;

//main object
WiFiManager wm;
AsyncWebServer server(80);

//Html template
extern String loginPage;
extern String loginPageError;
extern String mainPage_template;

//function
void callbackbutton();
void checkButton(float time);
void startServer();

void setup() {
  Serial.begin(115200);    
  
  pinMode(BUTTON_PINr, INPUT_PULLUP);
  pinMode(LED_BUTTONr, OUTPUT);

  digitalWrite(LED_BUTTONr, HIGH);
  //wm.resetSettings();

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
  Serial.println(localIP);

  if (!MDNS.begin(host)) { //http://esp32.local
    Serial.println("Error setting up MDNS responder!");
    unsigned long begin_Time2 = millis();
    while (1){
      if (!MDNS.begin(host)){
        if ((millis() - begin_Time2) > 30000){
          Serial.println("Fail to inicialize mDNS. Passing");
          break;
        }
      }
      else{
        Serial.println("mDNS responder started");
        break;
      }
    }
  }
  else{
    Serial.println("mDNS responder started");
  }
  
  startServer();
  attachInterrupt(digitalPinToInterrupt(BUTTON_PINr), callbackbutton, RISING);

  digitalWrite(LED_BUTTONr, LOW);
}

void loop() {
  if(buttonLock){
    checkButton(15);  
    buttonLock = false;
  }

  if(digitalRead(BUTTON_PINr) == HIGH){
    lastStateButton = true;
  }

  // reconect wi-fi in case of disconnect 
  if (WiFi.status() != WL_CONNECTED){
    Serial.println("lose connect, trying reconect");
    WiFi.begin();
    while(WiFi.status() != WL_CONNECTED){
      Serial.print(".");
      delay(500);
    }
    Serial.println("\nReconnected");
    startServer();
  }
  
  else{
    Serial.println('main code');  
  };]
}


