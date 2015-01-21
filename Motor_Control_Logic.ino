#include <AFMotor.h>
#include<string.h>

// Connect a stepper motor with 48 steps per revolution (7.5 degree)
// to motor port #2 (M3 and M4)
AF_Stepper motor(200, 1);
AF_Stepper motor2(200, 2);
int steps = 1;
int spd = 75;


String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  motor.setSpeed(spd);

  motor2.setSpeed(spd); 
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) 
  {
    
    if (inputString == "F\n")
    {
      motor.step(steps, FORWARD, DOUBLE);
    } 
    
    else if (inputString == "R\n")
    {
      motor.step(steps, BACKWARD, DOUBLE);
    }
    else if (inputString == "F2\n")
    {
      motor2.step(steps, FORWARD, DOUBLE); 
    }
    
    else if (inputString == "R2\n")
    {
      motor2.step(steps, BACKWARD, DOUBLE); 
    } 
    
    else if (inputString[0] == 'N')
    {
      steps = inputString.substring(1).toInt();
    }
    
    else if (inputString[0] == 'S')
    {
      spd = inputString.substring(1).toInt();
      
      motor.setSpeed(spd);

      motor2.setSpeed(spd); 
    }
    
    inputString = "";
    stringComplete = false;
    
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}



  
  
