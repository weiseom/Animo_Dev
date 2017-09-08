int trigPin3 = 8;
int echoPin3 = 9;
 
int trigPin2 = 10;
int echoPin2 = 11;

int trigPin1 = 12;
int echoPin1 = 13;
 
void sendSig(int trigNum);
void getDist(int echoNum);
 
void setup() {
  Serial.begin (9600);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
}
void loop() {

  sendSig(trigPin1);
  getDist(echoPin1);

  sendSig(trigPin2);
  getDist(echoPin2);
    
  sendSig(trigPin3);
  getDist(echoPin3);
  delay(300);
  
}
void sendSig(int trigNum){
  digitalWrite(trigNum, LOW);
  delayMicroseconds(2); 
  digitalWrite(trigNum, HIGH);
  delayMicroseconds(10); 
  digitalWrite(trigNum, LOW);
}

void getDist(int echoNum){
  
  long duration, distance;
    
  duration = pulseIn(echoNum, HIGH);
  distance = duration/2/29.1;

  Serial.print(echoNum-6);
  Serial.print(" ");
  Serial.print(distance);
  Serial.print("\n");  
  
}

