#include <ESP8266WiFi.h>
#include <Servo.h>

const char ssid[] = "Froggy-the-bot";
const char password[] = "12345678";
WiFiServer server(80);

int PinLED = 5;

Servo Servo0;
Servo Servo1;
Servo Servo2;
Servo Servo3;
Servo Servo4;
Servo Servo5;
Servo Servo6;
Servo Servo7;

void setup() {

	// servo gpio pins on node mcu
	Servo0.attach(1);
	Servo1.attach(2);
	Servo2.attach(3);
	Servo3.attach(4);
	Servo4.attach(5);
	Servo5.attach(6);
	Servo6.attach(7);
	Servo7.attach(8);

  Serial.begin(115200);

  pinMode(PinLED, OUTPUT);
  digitalWrite(PinLED, LOW);

  server.begin();
  WiFi.mode(WIFI_AP);
  WiFi.softAP(ssid, password);

  Serial.println();

	// print ip address
  Serial.print("IP Address: ");
	Serial.println(WiFi.softAPIP()); 
}

int getServoValue(char servoName, String url){
	int index = url.indexOf(servoName);
	String number = url.substring(index+2, index+5);
	return number.toInt();
}

void loop() 
{
  // Comprueba si el cliente ha conectado
  WiFiClient client = server.available();  
  if (!client) {
    return;
  }

  // Espera hasta que el cliente envía alguna petición
  Serial.println("nuevo cliente");
  while(!client.available()){
    delay(1);
  }

	String request = client.readStringUntil('r');

	int S0 = getServoValue('S0', request);
	int S1 = getServoValue('S1', request);
	int S2 = getServoValue('S2', request);
	int S3 = getServoValue('S3', request);
	int S4 = getServoValue('S4', request);
	int S5 = getServoValue('S5', request);
	int S6 = getServoValue('S6', request);
	int S7 = getServoValue('S7', request);

	Serial.printf("Servo values: S0 = %d, S1 = %d, S2 = %d, S3 = %d, S4 = %d, S5 = %d, S6 = %d, S7 = %d", 
							 S0, S1, S2, S3, S4, S5, S6, S7);

	Servo0.write(S0);
	Servo0.write(S1);
	Servo1.write(S2);
	Servo2.write(S3);
	Servo3.write(S4);
	Servo4.write(S5);
	Servo5.write(S6);
	Servo6.write(S7);

  // Envía la página HTML de respuesta al cliente
  client.println("HTTP/1.1 200 OK");
  client.println("");
  client.println("<!DOCTYPE HTML>");
  client.println("<meta charset='UTF-8'>");
  client.println("<html>");
  client.println("Hola lindo :v");
  client.println("</html>"); 
  delay(1);
}
