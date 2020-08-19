#include <Servo.h>
#include <CircularBuffer.h>

#define SERVO_1 5 // Porta Digital 6 PWM
#define SERVO_2 11 // Porta Digital 7 PWM

//posição inicial para qual o servo deve se deslocar no começo das rotinas
#define posicaoInicialMotor_1 90 
#define posicaoInicialMotor_2 65

Servo s1; // Variável Servo 1
Servo s2; // Variável Servo 2
uint16_t pos_1; // Posição Servo
uint16_t pos_2; // Posição Servo
int mot; // motor selecionado
CircularBuffer<byte,100> bytes;     // uses 538 bytes
CircularBuffer<byte,10> bufHandShake;     // uses 538 bytes
char data;
char data_1;
char data_2;
char buf[5];

bool flagConectado = false;

const byte ST = 0x24; //start
const byte ET = 0x5b; //final
const byte M1 = 0x25; //motor_1
const byte M2 = 0x2a; //motor_2
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

  /*if(!flagConectado){
    handShake();
  }*/
  
  //Serial.println("serial?: " + String(Serial.available()));
  if(Serial.available()){
    byte val = Serial.read();
    //Serial.println("valor lido pela serial: " + String(val));
    
    bytes.push(val); 
    
  }
  //Serial.println("tamanho do buffer: " + String(bytes.size()));
  if(bytes.size()>7){
    readData();
  }
}

const byte HS1 = 0x24; //recebe
const byte HSS = 0x5b; //envia
const byte HS2 = 0x25; //recebe
const byte HSF = 0x27; //envia

void handShake(){
  byte val = Serial.read();
  if(val == HS1){
    Serial.write(HSS);
    delay(1000);
    byte dat = Serial.read();
    dat = Serial.read();
    Serial.println(dat,DEC);
    /*if(dat == HS2){
      Serial.write(HSF); 
      flagConectado = true;
    }*/
  }
}

void readData(){
  bool flag = true;
  while(flag){
    byte data = bytes.shift();
    if(data == ST){
      //Serial.println("entrou no primeiro if");
      data = bytes.shift();
      if(data == QT){
        //Serial.println("entrou no segundo if");  
        //Validação se os valores inseridos são valores numéricos válidos
        byte motor_1 = bytes.shift();
        pos_1 = bytes.shift();
        byte motor_2 = bytes.shift();
        pos_2 = bytes.shift();
        byte dataFinal = bytes.shift();
        if(pos_1 >= 0 && pos_1 <=180 && motor_1 == M1 && dataFinal == ET){
          //Serial.println("motor 1");
          s1.write(pos_1);
          //delay(15);
          if(pos_2 >= 0 && pos_2 <=130 && motor_2 == M2 && dataFinal == ET){
            //Serial.println("motor 2");
            s2.write(pos_2);
          }
        }else{
          //Serial.println("else - final");
          flag = false; 
        }
       }else{
        //Serial.println("else - segundo if");
        flag = false; 
       }
    }else{
      //Serial.println("else - primeiro if");
      flag = false;
    }
  }
}
