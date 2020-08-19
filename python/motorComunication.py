import serial
import numpy as np
from threading import Timer
import time 

class motorCommunication:

    i = 0
    def main():
        global ser 
        global pos
        i = 0
        ser = serial.Serial('/dev/ttyACM0',115200, timeout=1)
        
       
        '''
        protocolo:
            const byte ST = 0x24; //start
            const byte QT = 0x27; //quantidade de informação (não estou usando de verdade, mas a validação está sendo feita)
            const byte M1 = 0x25; //motor_1
                            valor // posição_1
            const byte M2 = 0x26; //motor_2
                            valor // posição_2
            const byte ET = 0x5b; //final
        '''
        a = '%' #motor 1
        b = '*' #motor 2

        

        #create the input
        i1 = np.linspace(50,180,131)
        i2 = np.linspace(180,50,131)
        i3 = np.linspace(50,180,131)
        i4 = np.linspace(180,50,131)
        i5 = np.linspace(50,180,131)
        i6 = np.linspace(180,50,131)
        i7 = np.linspace(50,180,131)
        i8 = np.linspace(180,50,131)
        i9 = np.linspace(50,180,131)
        pos = np.concatenate((i1,i2,i3,i4,i5,i6,i7,i8,i9))
  
        for val in pos:
            motorCommunication.sendValue(b,int(val))
            time.sleep(0.1)

        ser.close()


    def sendValue(motor,posicao):
        ser.write(b'$')
        ser.write(b"'")
        ser.write(b'%')        
        ser.write(bytes([posicao])) 
        ser.write(b'*')        
        ser.write(bytes([posicao])) 
        ser.write(b'[')


if __name__ == '__main__':
    motorCommunication.main()