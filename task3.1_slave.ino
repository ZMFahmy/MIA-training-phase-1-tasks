#include <Wire.h>

int LED = 13;

void setup()
{
  Wire.begin(4); 
  Wire.onReceive(reading_recieved);
  Serial.begin(9600);
  
  pinMode(LED, OUTPUT);
}

void reading_recieved(int bytes) 
{
  int x = Wire.read();
  
  if(x == 0)
  {
    analogWrite(LED, 0);
    Serial.println("No message");
  }
  
  else if(x == 1)
  {
    analogWrite(LED, 155); 
    Serial.println("Vector focused");
  }
    
  else if(x == 2)
  {
    analogWrite(LED, 192);
    Serial.println("Vector distracted");
  }
   
  else
  {
    analogWrite(LED, 255);
    Serial.println("Glitch");
  }
}

void loop()
{   
  delay(500);
}
