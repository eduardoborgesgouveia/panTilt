from matplotlib.colors import hsv_to_rgb
import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
import colorsys


# blue = colorsys.rgb_to_hsv(1.0, 0.80, 0.0)
# blue_2 = colorsys.rgb_to_hsv(0, 0, 1)
blue =   np.array([0.6666666666666666, 1.0, 0.5450980392156862])
blue_2 = np.array([240,100,54])
# blue = np.array([0,0,139])
# blue_2 = np.array([0,0,255])

lo_square = np.full((10, 10, 3), blue) 
do_square = np.full((10, 10, 3), blue_2)

plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.show()