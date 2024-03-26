extern String generateDynamicData();

String generateDynamicData() {
  return "Dados do ESP32!\n";
}

//-----------------------------------------------------------------------------------------------------------------------
// Callback function's for web server

void handleMessage(AsyncWebServerRequest *request){
  String message;
  if (request->hasParam("message", true)) {
    message = request->getParam("message", true)->value();
    Serial.println("Mensagem recebida: " + message);
  }
  request->send(200, "text/plain", "Dados recebidos com sucesso");
}

void handleDataCheck(AsyncWebServerRequest *request){
  String dynamicData = generateDynamicData();
  request->send(200, "text/plain", dynamicData);
}

void handleFailLogin(AsyncWebServerRequest *request){
  request->send(200, "text/html", loginPageError);
}

void handleRoot(AsyncWebServerRequest *request) {
  request->send(200, "text/html", loginPage);
}

void handleAdminIndex(AsyncWebServerRequest *request) {
  request->send(200, "text/html", mainPage_template);
}

void handleLogin(AsyncWebServerRequest *request){
  String userid = request->getParam(0)->value();
  String pwd = request->getParam(1)->value();
      
  if (userid.equals(User) && pwd.equals(Password)) {
    Serial.println("Admin e Senha Aprovados");
    request->redirect("/AdminIndex"); 
    return;
  }

  else{
    request->redirect("/Faillogin"); 
  }
}

void handleUpdateCallback(AsyncWebServerRequest *request) {
  AsyncWebServerResponse *response = request->beginResponse(200, "text/plain", (Update.hasError()) ? "FAIL" : "OK");
  response->addHeader("Connection", "close");
  request->send(response);
  if (!Update.hasError()) {
    ESP.restart();
  }
}

void handleUpdateFileCallback(AsyncWebServerRequest *request, String filename, size_t index, uint8_t *data, size_t len, bool final) {
  if (!index) {
    Serial.printf("Update: %s\n", filename.c_str());
    if (!Update.begin(UPDATE_SIZE_UNKNOWN)) {
      Update.printError(Serial);
    }
  }
  if (Update.write(data, len) != len) {
    Update.printError(Serial);
  }
  if (final) {
    if (Update.end(true)) {
      Serial.printf("Update Success: %u\nRebooting...\n", index + len);
    } else {
      Update.printError(Serial);
    }
  }
}

//-----------------------------------------------------------------------------------------------------------------------
// Start Server

void startServer(){
  server.on("/", HTTP_GET, handleRoot); 
  server.on("/AdminIndex", HTTP_GET, handleAdminIndex); 
  server.on("/login", HTTP_POST, handleLogin);
  server.on("/Faillogin", HTTP_POST, handleFailLogin);
  server.on("/update", HTTP_POST, handleUpdateCallback, handleUpdateFileCallback);
  server.on("/getData", HTTP_GET, handleDataCheck);
  server.on("/receveData", HTTP_POST, handleMessage);
  server.begin();
}

