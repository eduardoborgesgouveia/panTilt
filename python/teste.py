import numpy as np
import cv2
import matplotlib.pyplot as plt
from segmentationUtils import segmentationUtils
import matplotlib.patches as patches
class teste:
    def main():
        rects = []
        texts = []
        cap = cv2.VideoCapture(2)
        fig,axarr = plt.subplots(1)
        handle = None
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #cv2.normalize(frame, frame, 0, 255, cv2.NORM_MINMAX)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
            h, s, v = cv2.split(frame)
            v += 255
            s_1 = s * 0.9
            final_hsv = cv2.merge((h, np.uint8(s_1), v))
            frame = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB) 
            
            detection  = segmentationUtils.watershed(frame,'--neuromorphic',minimumSizeBox=0.5,smallBBFilter=True,centroidDistanceFilter = True, mergeOverlapingDetectionsFilter = True,flagCloserToCenter=True)

            teste.cleanFigure(rects,texts)
            for j in range(len(detection)):
                rect = patches.Rectangle((detection[j][1],detection[j][0]),detection[j][3],detection[j][2],linewidth=1,edgecolor='r',facecolor='none')
                plt.gca().add_patch(rect)
                rects.append(rect)
                

            if handle is None:
                handle = plt.imshow(frame)
            else:
                handle.set_data(frame)

            plt.pause(0.01)
            plt.draw()
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def cleanFigure(rects = [],texts = []):
        for s in range(len(rects)):
            rects[s].set_visible(False)

        for s in range(len(texts)):
            texts[s].set_visible(False)   



if __name__ == '__main__':
    teste.main()