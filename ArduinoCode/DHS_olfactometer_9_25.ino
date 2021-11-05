
String myname="Olfactometer3";
#include <Arduino_HTS221.h>
#include <Arduino_LPS22HB.h>

#define BUFFER_SIZE 40
#define stp A4
#define dir A5
#define MS1 A6
#define MS2 A7
#define EN  8

unsigned int val;
char buffer[BUFFER_SIZE];
char user_input;
long waittime;
long IRstart;
int exitflag;
int x;
long pokeStart;
int fanPin=9;
float temperature;

float humidity;
float pressure;
int feedpin=11;
float sniffTime=4000;


int msg;
int pin;
int irpin=10;




void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
  while (!Serial);

  if (!HTS.begin()) {
    Serial.println("Failed to initialize humidity temperature sensor!");
    while (1);}
    
  pinMode(irpin, INPUT_PULLUP);
  pinMode(feedpin, INPUT);
  pinMode(stp, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
  pinMode(EN, OUTPUT);
  resetEDPins(); //Set step, direction, microstep and enable pins to default states
  HTS.begin();
  BARO.begin(); 
  
}


void loop() {
// put your main code here, to run repeatedly:
//Check for Messages on Serial Port and Address them
   msg=ReadData();
   //If msg is 1, run Activate Valve function
   if (msg ==1)
      {ActivateValve();}
   
   else if (msg==2)
      {DeactivateValve();}
   
   else if (msg==4)
      {WhatIsYourName();} 
   
   else if (msg==5)
      {checkIR();} 
   
   else if (msg==6)
      {Panelup();}
  
   else if (msg==7)
      {Paneldown();}
  
   else if (msg==8)
      {Runfeeder();}
   
   else if (msg==9)
      {
         temperature = HTS.readTemperature();
         Serial.println(temperature);}
      
   else if (msg==10)
      {humidity = HTS.readHumidity();
        Serial.println(humidity);}

   else if (msg==11)
      { pressure= BARO.readPressure();
        Serial.println(pressure);}

   else if (msg==12)
      {digitalWrite(fanPin, HIGH);}

   else if (msg==13)
      {digitalWrite(fanPin, LOW);}

   else if (msg==14)//set sniff criterion 
      {sniffTime=ReadData();}
      
}




//Read Serial Data
int ReadData() { 
 int index=0; 
while(1){
if (Serial.available() > 0) {
    bool ready = false;
    int value;
    int inChar = Serial.read();
    buffer[index] = (char) inChar;
    index++;
    if (index >= BUFFER_SIZE) {
      index = BUFFER_SIZE - 1;
      ready = true;
    }

    if (inChar == '\n' || inChar == '\r') {
      ready = true;
    }

    if (ready) {
      if (isdigit(buffer[0]) || buffer[0] == '-') {
        buffer[BUFFER_SIZE - 1] = '\0';
        value = atoi(buffer);
        //Serial.println(value);
        //Serial.println("Enter a integer, with a linefeed at the end");
      }
      index = 0;
      return(value);
    }
  }
}}


void ActivateValve()
{
  pin=ReadData();
  if (pin==1){
      pin=A3;
    }
   else if(pin==2){
      pin=A2;
    }
   else if(pin==3){
      pin=A1;
    }
   else if(pin==4){
      pin=A0;
    }
   else if(pin==5){
      pin=13;
    }
   else if(pin==6){
      pin=12;
    }
  
  pinMode(pin, OUTPUT);
  digitalWrite(pin, HIGH);  
}

void DeactivateValve()
{
  //Serial.println("Valve to Deactivate");
  pin=ReadData();
  
    if (pin==1){
      pin=A3;
    }
   else if(pin==2){
      pin=A2;
    }
   else if(pin==3){
      pin=A1;
    }
   else if(pin==4){
      pin=A0;
    }
   else if(pin==5){
      pin=13;
    }
   else if(pin==6){
      pin=12;
    }
    
  pinMode(pin, OUTPUT);
  digitalWrite(pin, LOW);
}

void WhatIsYourName(){
  Serial.println(myname);
}


void checkIR(){
  waittime=10;
  exitflag=0;
  IRstart=millis();
  
  while (exitflag==0){

  if (millis()-IRstart> waittime){
    Serial.println("0");
    exitflag=1;
  }
  
  if(digitalRead(irpin)==LOW){
    pokeStart=millis(); //Record Time of start of poke
    
    //Go into a loop unitl
    while (exitflag==0){
    
    //Dog either removes their nose 
      if (digitalRead(irpin)==HIGH){
        //Print out the length of nose hold
        Serial.println(millis()-pokeStart);
        exitflag=1;
        }
    
    //or Holds nose in 4s 
      if (millis()-pokeStart>sniffTime){ 
        //Print out the length of nose hold
        Serial.println(millis()-pokeStart);
        exitflag=1;
      }}
  }
}
}



void Paneldown(){
  exitflag=0; //Escape the motor movement
  digitalWrite(EN, LOW);
  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  for(x= 1; x<4500; x++)  //Loop the forward stepping enough times for motion to be visible
  { 
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(1); 
  
  } 
  resetEDPins();
}

void Panelup(){
  exitflag=0; //Escape the motor movement
  digitalWrite(EN, LOW);
  digitalWrite(dir, HIGH); //Pull direction pin low to move "Reverse"
  for(x= 1; x<4500; x++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(1);
    
  } 
  resetEDPins();
}




void Runfeeder(){
  pinMode(feedpin, OUTPUT);
  digitalWrite(feedpin, LOW);
  delay(500);
  pinMode(feedpin, INPUT_PULLUP);
}


void resetEDPins()
{
  digitalWrite(stp, LOW);
  digitalWrite(dir, LOW);
  digitalWrite(MS1, LOW);
  digitalWrite(MS2, LOW);
  digitalWrite(EN, HIGH);
}
