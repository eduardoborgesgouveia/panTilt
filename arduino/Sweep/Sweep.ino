/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
Servo myservo_2;
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(11);  // attaches the servo on pin 9 to the servo object
  myservo_2.attach(5);
}

void loop() {
  for (pos = 0; pos <= 130; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo_2.write(pos);// tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    myservo.write(pos);   
  }
  for (pos = 130; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo_2.write(pos);         // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    myservo.write(pos);
  }
}
