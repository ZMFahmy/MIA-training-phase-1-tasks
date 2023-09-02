#include <Wire.h>

const int push_button_1 = 12;
const int push_button_2 = 13;

int button_1_val = 0;
int button_2_val = 0;
int sent_value = 0;

void setup()
{
  Wire.begin(); 
  Serial.begin(9600);
  
  pinMode(push_button_1,INPUT_PULLUP);
  pinMode(push_button_2,INPUT_PULLUP);  
}

void loop()
{
  button_1_val = digitalRead(push_button_1);
  button_2_val = digitalRead(push_button_2);
  
  if(button_1_val == HIGH && button_2_val == HIGH)
    sent_value = 0;
  
  else if(button_1_val == LOW && button_2_val == HIGH)
    sent_value = 1;
    
  else if(button_1_val == HIGH && button_2_val == LOW)
    sent_value = 2;
    
  else
    sent_value = 3;
    
  Serial.print(sent_value);
    
  
  Wire.beginTransmission(4);
  Wire.write(sent_value);       
  Wire.endTransmission(); 
  delay(500);
}
