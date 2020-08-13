int led = 10;           
int br = 0;    
int fa;    
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  analogWrite(led,br);
}
void loop() {
  
 while(!Serial.available())
 {
 br = Serial.read()
 analogWrite(led,br);
  
   }
}
