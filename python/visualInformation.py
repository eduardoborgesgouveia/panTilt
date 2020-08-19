import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 
import imutils
from segmentationUtils import segmentationUtils
import matplotlib.patches as patches
import math
import serial
import time 

class visualInformation:
    def main():
        font = {'family': 'serif',
            'color':  'white',
            'weight': 'normal',
            'size': 8,
        }
        fig,axarr = plt.subplots(1)
        handle = None
        global imageDimensions
        global comunicacaoSerial 
        comunicacaoSerial = serial.Serial('/dev/ttyACM0',115200, timeout=1)
        angulos = np.linspace(0,180,90)
        contador = 0
        flag = False
        a = '%' #motor 1
        b = '*' #motor 2
        rects = []
        texts = []
        pos_atual_x = 90
        pos_atual_y = 65
        cap = cv.VideoCapture(2)
        if(cap.isOpened() == False):
            print('erro ao abrir arquivo') 
        else:
            while(cap.isOpened()):
                ret, frame = cap.read()
                
                if(ret == False):
                    break
                #640
                #480
                imageDimensions = frame.shape
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                frame = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
                h, s, v = cv.split(frame)
                v += 255
                s_1 = s * 0.9
                final_hsv = cv.merge((h, np.uint8(s_1), v))
                frame = cv.cvtColor(final_hsv, cv.COLOR_HSV2RGB) 
                
                detection  = segmentationUtils.watershed(frame,'--neuromorphic',minimumSizeBox=0.5,smallBBFilter=True,centroidDistanceFilter = True, mergeOverlapingDetectionsFilter = True,flagCloserToCenter=True)

                distance, x_distance, y_distance = visualInformation.getError(detection)
                
                
                if x_distance is not None and x_distance < 0:
                    pos_atual_x += (abs(x_distance)/100)
                    if pos_atual_x >= 180:
                        pos_atual_x = 180
                    # visualInformation.sendValue(a,int(pos_atual_x))
                elif x_distance is not None and x_distance > 0:
                    pos_atual_x -= (abs(x_distance)/100)
                    if pos_atual_x <= 0:
                        pos_atual_x = 0
                    # visualInformation.sendValue(a,int(pos_atual_x))
                #time.sleep(0.200)
                if y_distance is not None and y_distance > 0:
                    pos_atual_y += (abs(y_distance)/100)
                    if pos_atual_y >= 130:
                        pos_atual_y = 130
                    # visualInformation.sendValue(b,int(pos_atual_y))
                elif y_distance is not None and y_distance < 0:
                    pos_atual_y -= (abs(y_distance)/100)
                    if pos_atual_y <= 0:
                        pos_atual_y = 0
                    # visualInformation.sendValue(b,int(pos_atual_y))
                visualInformation.sendValue(pos_atual_x,pos_atual_y)
                # 
                # if(not flag):
                #     visualInformation.sendValue(a,int(angulos[contador]))
                #     contador = contador + 1
                #     if contador >= 89:
                #         flag = True
                # else:
                #     visualInformation.sendValue(a,int(angulos[contador]))
                #     contador = contador - 1
                #     if contador <= 0:
                #         flag = False

                    
                print(y_distance, pos_atual_y)
                if handle is None:
                    handle = plt.imshow(frame)
                else:
                    handle.set_data(frame)
                        
                visualInformation.cleanFigure(rects,texts)
                for j in range(len(detection)):
                    rect = patches.Rectangle((detection[j][1],detection[j][0]),detection[j][3],detection[j][2],linewidth=1,edgecolor='r',facecolor='none')
                    plt.gca().add_patch(rect)
                    rects.append(rect)
                    text = plt.gca().text(1, 1, str(distance), fontdict = font,bbox=dict(facecolor='red', alpha=1))
                    texts.append(text)
                
                plt.pause(0.01)
                plt.draw()

        cap.release()
        cv.destroyAllWindows()


    def getError(detection):
        distanceToCenter = None
        x_distance = None
        y_distance = None
        if len(detection) > 0:
            distanceToCenter = math.sqrt(((detection[0][4]-imageDimensions[1]/2)**2)+((detection[0][5]-imageDimensions[0]/2)**2))
            x_distance = detection[0][5]-(imageDimensions[1]/2)
            y_distance = detection[0][4]-(imageDimensions[0]/2)
        return distanceToCenter,x_distance,y_distance

    def cleanFigure(rects = [],texts = []):
        for s in range(len(rects)):
            rects[s].set_visible(False)

        for s in range(len(texts)):
            texts[s].set_visible(False)     
    def sendValue(posicao_x,posicao_y,motor =None):
        # comunicacaoSerial.write(b'$')
        # comunicacaoSerial.write(b"'")
        # comunicacaoSerial.write(motor.encode())        
        # comunicacaoSerial.write(bytes([posicao])) 
        # comunicacaoSerial.write(b'[')

        comunicacaoSerial.write(b'$')
        comunicacaoSerial.write(b"'")
        comunicacaoSerial.write(b'%')        
        comunicacaoSerial.write(bytes([int(posicao_x)])) 
        comunicacaoSerial.write(b'*') 
        comunicacaoSerial.write(bytes([int(posicao_y)]))
        comunicacaoSerial.write(b'[')  

       

if __name__ == '__main__':
    visualInformation.main()