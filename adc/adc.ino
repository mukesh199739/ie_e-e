void setup() {
  // put your setup code here, to run once:
pinMode(A4,INPUT);
pinMode(A5,INPUT);
Serial.begin(9600);
}

void loop() 
{
  int x=analogRead(A4);
  delay(1000);
  //Serial.println(x);
  int y=analogRead(A5);
  if(x<90) 
  {
    Serial.println("y");
  }
  else if(y<90)
  {
    Serial.println("g");
  }
  else
  {
    Serial.println("no site selected");
  }
  
}
