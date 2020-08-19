#include <Servo.h>


#define SERVO_1 6 // Porta Digital 6 PWM
#define SERVO_2 7 // Porta Digital 7 PWM

//posição inicial para qual o servo deve se deslocar no começo das rotinas
#define posicaoInicialMotor_1 90 
#define posicaoInicialMotor_2 130

Servo s1; // Variável Servo 1
Servo s2; // Variável Servo 2
int pos; // Posição Servo
int mot; // motor selecionado

String data;


void setup ()
{
  s1.attach(SERVO_1);
  s2.attach(SERVO_2);
  
  //ajustando a posição incial do PanTilt
  s1.write(posicaoInicialMotor_1);
  delay(200);
  s2.write(posicaoInicialMotor_2);
  
  Serial.begin(9600);
    
}
 
void loop()
{
  while (Serial.available() > 0) {
    data = Serial.readString();// Lendo os valores 
    //Os valores devem vir no formato " 'motor':'posicao' "
    String motor = getValue(data, ':', 0);
    String posicao = getValue(data, ':', 1);
    //Diagnosticos
    Serial.print("motor: " + motor); 
    Serial.print(" | ");
    Serial.println("posição: "+posicao);
    //Validação se os valores inseridos são valores numéricos válidos
    if(isValidNumber(posicao) && isValidNumber(motor)){
      pos = posicao.toInt();
      mot = motor.toInt();
      Serial.println("comando: motor " + motor + " para posição " + posicao + "");
      //os valores de posição para o primeiro motor (motor da movimento em X) variam entre 0° e 180°
      if(pos >= 0 && pos <=180 && mot == 1){
          s1.write(pos);
      //os valores de posição para o segundo motor (motor de movimento em Y) variam entre 50° e 180°
      }else if(pos >= 50 && pos <=180 && mot == 2){
          s2.write(pos); 
      }else{
         Serial.println("O motor " + motor + " não pode se mover para o valor determinado (valor desejado: " + posicao+")");
      }
    }else{
      Serial.println("Não é um valor válido");
    }
  }
}
//função SPLIT da string
String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
//verificação dos números
boolean isValidNumber(String str){
   for(byte i=0;i<str.length();i++)
   {
      if(isDigit(str.charAt(i))) return true;
        }
   return false;
} 