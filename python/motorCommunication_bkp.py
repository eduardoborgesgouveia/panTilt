import serial
import numpy as np
from threading import Timer

class motorCommunication:

    i = 0
    def main():
        global ser 
        global pos
        i = 0
        ser = serial.Serial('/dev/ttyACM0',115200, timeout=1)
        
       
        '''
            const byte ST = 0x24; //start
            const byte ET = 0x5b; //final
            const byte M1 = 0x25; //motor_1
            const byte M2 = 0x26; //motor_2
            const byte QT = 0x27; //quantidade de informação
        '''
        a = '%' #motor 1
        b = '*' #motor 2
        # #tentar handshake
        # flagConectado = False
        # i = 0
        # while(not flagConectado):
        #     ser.write(b'$')
        #     resposta = ser.readline()
        #     if(resposta == b'['):
        #         ser.write(b'%')
        #         resposta = ser.readline()
        #         if(resposta == b"'"):
        #             flagConectado = True
        

        #create the input
        i1 = np.linspace(0,180,181)
        i2 = np.linspace(180,0,181)
        i3 = np.linspace(0,180,181)
        i4 = np.linspace(180,0,181)
        i5 = np.linspace(0,180,181)
        i6 = np.linspace(180,0,181)
        i7 = np.linspace(0,180,181)
        i8 = np.linspace(180,0,181)
        i9 = np.linspace(0,180,181)
        pos = np.concatenate((i1,i2,i3,i4,i5,i6,i7,i8,i9))
        timer = RepeatTimer(1, motorCommunication.handleTimer())
        timer.start()
        
        # this will stop the timer
        #stopFlag.set()
        #for val in pos:
            #motorCommunication.sendValue(a,val)
            #motorCommunication.sendValue(a,int(val))

        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        ##ser.write(b'\x24\r')
        #ser.write(b'$')
        #print(ser.readline())
        #ser.write(b"'")
        ##ser.write(b'\x27\r')
        #print(ser.readline())
        #ser.write(b'%')
        #print(ser.readline())
        #ser.write(bytes([180]))
        #print(ser.readline())
        #ser.write(b'[')
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        #print(ser.readline())
        ser.close()


    def sendValue(motor,posicao):
        ser.write(b'$')
        #print(ser.readline())
        ser.write(b"'")
        #print(ser.readline())
        ser.write(motor.encode())
        #print(ser.readline())
        ser.write(bytes([posicao]))
        #print(ser.readline())    
        ser.write(b'[')
        #print(ser.readline())
    
    def handleTimer():
        #motorCommunication.sendValue('%',int(pos[i]))
        print("tô funcionando")
        #i = i + 1

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


if __name__ == '__main__':
    motorCommunication.main()