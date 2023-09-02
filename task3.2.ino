const int trigPin_left = 9;
const int echoPin_left = 10;
const int trigPin_down = 11;
const int echoPin_down = 12;

long left_duration;
int x_coordinate;

long down_duration;
int y_coordinate;

void setup() {
  pinMode(trigPin_left, OUTPUT); 
  pinMode(echoPin_left, INPUT); 
  pinMode(trigPin_down, OUTPUT); 
  pinMode(echoPin_down, INPUT); 

  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin_left, LOW);
  digitalWrite(trigPin_down, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin_left, HIGH);
  digitalWrite(trigPin_down, HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trigPin_left, LOW);
  digitalWrite(trigPin_down, LOW);

  left_duration = pulseIn(echoPin_left, HIGH);
  x_coordinate = left_duration * 0.034 / 2;
  down_duration = pulseIn(echoPin_down, HIGH);
  y_coordinate = down_duration * 0.034 / 2;

  Serial.print("x: ");
  Serial.print(x_coordinate);
  Serial.print("      y: ");
  Serial.println(y_coordinate);
}
