extern String Proj_Name;
extern String Autores; 
extern String data;
extern String Version;
extern String generateDynamicData();
//-----------------------------------------------------------------------------------------------------------------------
// HTML tamplate for main admin page

String mainPage_template = "<!DOCTYPE html>\
<html lang='en'>\
    <head>\
        <title>" + Proj_Name + "</title>\
        <style>\
            body {\
                background-color: #2c2c2c;\
                color: white;\
                margin: 50px;\
            }\
            #content {\
                display: flex;\
                flex-direction: column;\
                align-items: center;\
                justify-content: center;\
                height: 100vh;\
            }\
            .container {\
                background-color: #2A6190;\
                border: 2px solid #000000;\
                border-radius: 10px;\
                padding: 20px;\
                width: 100%;\
                margin: 10px;\
            }\
            .divider {\
                border-top: 2px solid #ccc;\
                margin-top: 15px;\
                margin-bottom: 20px;\
            }\
            .centered-text {\
                text-align: center;\
            }\
            #console_container {\
                width: 100%;\
                box-sizing: border-box;\
            }\
            #console_output {\
                width: 100%;\
                height: calc(100% - 40px);\
                resize: none;\
            }\
            .input-container {\
                display: flex;\
                justify-content: space-between;\
                align-items: center;\
            }\
            .input-container input[type='text'] {\
                flex-grow: 1;\
                margin-left: 5px;\
                margin-right: 5px;\
            }\
            .footer {\
                position: sticky;\
                bottom: 0;\
                right: 0;\
                padding: 1px;\
                background-color: #2c2c2c;\
                color: #ffffff;\
                font-size: 10px;\
                z-index: -999;\
            }\
        </style>\
        <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>\
        <script>\
          function updateConsole(message) {\
            var consoleOutput = document.getElementById('console_output');\
            consoleOutput.value += message;\
            consoleOutput.scrollTop = consoleOutput.scrollHeight;\
          }\
          function sendToConsole() {\
            var xhr = new XMLHttpRequest();\
            xhr.open('GET', '/getData', true);\
            xhr.onload = function() {\
              if (xhr.status == 200) {\
                updateConsole(xhr.responseText);\
              }\
            };\
            xhr.send();\
          }\
        </script>\
    </head>\
    <body>\
        <div id='content'>\
            <div class='container'>\
                <h1>" + Proj_Name + "</h1>\
                <button onclick='sendToConsole()'>GET Info</button>\
                <div class='divider'></div>\
                <h2 class='centered-text'>Output</h2>\
                <div id='console_container'>\
                    <textarea class='text-secondary form-control' id='console_output' rows='15'></textarea>\
                </div>\
                <div class='divider'></div>\
                <div class='input-container'>\
                    <label for='message' class='centered-text'>Comando: </label>\
                    <input type='text' id='message'>\
                    <button id='sendButton' class='centered-text'>Enviar</button>\
                </div>\
                <script>\
                    document.addEventListener('DOMContentLoaded', function () {\
                        var sendButton = document.getElementById('sendButton');\
                        var messageInput = document.getElementById('message');\
                        sendButton.addEventListener('click', function () {\
                            var message = messageInput.value;\
                            var xhr = new XMLHttpRequest();\
                            xhr.open('POST', '/receveData', true);\
                            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');\
                            xhr.send('message=' + encodeURIComponent(message));\
                            messageInput.value = '';\
                        });\
                    });\
                </script>\
                <br></br>\
                <div class='centered-text'>\
                    <form method='POST' action='#' enctype='multipart/form-data' id='upload_form'>\
                    <input type='file' name='update'>\
                    <input type='submit' value='Update'>\
                    </form>\
                </div>\
                <div id='prg' class='centered-text'>progresso: 0%</div>\
            </div>\
            <div class='footer'>\
                <p>" + Autores +" : " + data + " : V" + Version + " : IOT connection to " + Proj_Name + "</p>\
            </div>\
        </div>\
        <script>\
          $('form').submit(function(e){\
            e.preventDefault();\
            var form = $('#upload_form')[0];\
            var data = new FormData(form);\
            $.ajax({\
              url: '/update',\
              type: 'POST',\
              data: data,\
              contentType: false,\
              processData:false,\
              xhr: function() {\
                var xhr = new window.XMLHttpRequest();\
                xhr.upload.addEventListener('progress', function(evt) {\
                  if (evt.lengthComputable) {\
                    var per = evt.loaded / evt.total;\
                    $('#prg').html('progress: ' + Math.round(per*100) + '%');\
                  }\
                }, false);\
                return xhr;\
              },\
              success:function(d, s) {\
                console.log('success!')\
              },\
              error: function (a, b, c) {\
            }\
          });\
        });\
        </script>\
    </body>\
</html>";

//-----------------------------------------------------------------------------------------------------------------------
// HTML tamplate for login page

String loginPage = "<!DOCTYPE html>\
<html>\
  <head>\
    <title>" + Proj_Name + "</title>\
    <style>\
      body {\
        text-align: center;\
        margin-top: 150px;\
        font-family: Arial, sans-serif;\
        background-color: #2c2c2c;\
      }\
      h1 {\
        font-size: 24px;\
          font-weight: bold;\
          color: #ffffff;\
      }\
      .login-container {\
        display: inline-block;\
        padding: 20px;\
        border-radius: 10px;\
        background-color: #2A6190;\
        color: #ffffff;\
        border: 2px solid #000000;\
      }\
      .login-form {\
          margin-top: 30px;\
      }\
      .form-field {\
        margin-bottom: 10px;\
      }\
      .form-field label {\
          display: block;\
          font-weight: bold;\
          margin-bottom: 5px;\
          color: #ffffff;\
      }\
      .form-field input {\
          width: 200px;\
          padding: 5px;\
      }\
      .login-button {\
          margin-top: 20px;\
      }\
      .footer {\
          position: fixed;\
          bottom: 0;\
          right: 0;\
          padding: 10px;\
          background-color: #2c2c2c;\
          color: #ffffff;\
          font-size: 15px;\
      }\
    </style>\
  </head>\
  <body>\
      <div class='login-container'>\
          <h1>Login Page</h1>\
          <form class='login-form' action='/login' method='POST'>\
              <div class='form-field'>\
                  <label for='username'>Username:</label>\
                  <input type='text' id='username' name='userid' required>\
              </div>\
              <div class='form-field'>\
                  <label for='password'>Password:</label>\
                  <input type='password' id='password' name='pwd' required>\
              </div>\
              <div class='login-button'>\
                  <input type='submit' value='Login'>\
              </div>\
          </form>\
      </div>\
      <div class='footer'>\
          <p>" + Autores + ": " + data + " : V" + Version + " : IOT connection to " + Proj_Name +"</p>\
      </div>\
  </body>\
</html>";

//-----------------------------------------------------------------------------------------------------------------------
// HTML tamplate for login error page

String loginPageError = "<!DOCTYPE html>\
<html>\
  <head>\
    <title>" + Proj_Name + "</title>\
    <style>\
      body {\
        text-align: center;\
        margin-top: 150px;\
        font-family: Arial, sans-serif;\
        background-color: #2c2c2c;\
      }\
      h1 {\
        font-size: 24px;\
          font-weight: bold;\
          color: #ffffff;\
      }\
      .login-container {\
        display: inline-block;\
        padding: 20px;\
        border-radius: 10px;\
        background-color: #2A6190;\
        color: #ffffff;\
        border: 2px solid #000000;\
      }\
      .login-form {\
          margin-top: 30px;\
      }\
      .form-field {\
        margin-bottom: 10px;\
      }\
      .form-field label {\
          display: block;\
          font-weight: bold;\
          margin-bottom: 5px;\
          color: #ffffff;\
      }\
      .form-field input {\
          width: 200px;\
          padding: 5px;\
      }\
      .login-button {\
          margin-top: 20px;\
      }\
      .footer {\
          position: fixed;\
          bottom: 0;\
          right: 0;\
          padding: 10px;\
          background-color: #2c2c2c;\
          color: #ffffff;\
          font-size: 15px;\
      }\
      .mensagem-erro {\
        font-weight: bold;\
        width: 250px;\
        height: 50px;\
        background-color: red;\
        border: 2px solid black;\
        color: white;\
        border-radius: 10px;\ 
        text-align: center;\
        line-height: 50px;\
        position: absolute;\
        top: calc(50% - 250px);\
        left: 50%;\
        transform: translateX(-50%);\
      }\
    </style>\
  </head>\
  <body>\
      <div class='mensagem-erro'>Usuario ou senha incorreta</div>\
      <div class='login-container'>\
          <h1>ESP32 Login Page</h1>\
          <form class='login-form' action='/login' method='POST'>\
              <div class='form-field'>\
                  <label for='username'>Username:</label>\
                  <input type='text' id='username' name='userid' required>\
              </div>\
              <div class='form-field'>\
                  <label for='password'>Password:</label>\
                  <input type='password' id='password' name='pwd' required>\
              </div>\
              <div class='login-button'>\
                  <input type='submit' value='Login'>\
              </div>\
          </form>\
      </div>\
      <div class='footer'>\
          <p>" + Autores + " : " + data + " : V" + Version + " : IOT connection to " + Proj_Name + "</p>\
      </div>\
  </body>\
</html>";