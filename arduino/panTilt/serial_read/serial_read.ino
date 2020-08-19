#include <Servo.h>
#include <CircularBuffer.h>

#define SERVO_1 6 // Porta Digital 6 PWM
#define SERVO_2 7 // Porta Digital 7 PWM

//posição inicial para qual o servo deve se deslocar no começo das rotinas
#define posicaoInicialMotor_1 90 
#define posicaoInicialMotor_2 130

Servo s1; // Variável Servo 1
Servo s2; // Variável Servo 2
int pos; // Posição Servo
int mot; // motor selecionado
CircularBuffer<byte,100> bytes;     // uses 538 bytes
char data;
char data_1;
char data_2;
char buf[5];

const byte ST = 0x24; //start
const byte ET = 0x5b; //final
const byte M1 = 0x25; //motor_1
const byte M2 = 0x26; //motor_2
const byte QT = 0x27; //quantidade de informação
byte LV = 0x30; //valor da posicao do motor --> LSB
byte MV = 0x30; //valor da posicao do motor --> MSB

void setup ()
{
  s1.attach(SERVO_1);
  s2.attach(SERVO_2);
  
  //ajustando a posição incial do PanTilt
  s1.write(posicaoInicialMotor_1);
  delay(200);
  s2.write(posicaoInicialMotor_2);
  
  Serial.begin(115200);
   
    
}
 
void loop()
{
  if (Serial.available()) {
    byte val = Serial.read();
    if(val != -1){
      bytes.push(val); 
      Serial.println(val);
    }
  }
}
