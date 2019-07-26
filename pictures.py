# cv2.IMREAD_COLOR para color, las transparencias se ignoran 1
# cv2.IMREAD_GRAYSCALE imagen en escala de grises 0 
# cv2.IMREAD_UNCHANGED  carga la imagen sin alteraciones -1

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

#The image must be in the same directory or enter the path
picture = input("Introduce el nombre y extension  de la imagen: ")

#Lee y muestra la imagen en color
img = cv2.imread(picture, cv2.IMREAD_UNCHANGED)
cv2.imshow('Imagen en Color', img)
cv2.waitKey(0)


#Lee, guarda y  muestra la imagen en escala de grises
bw = cv2.imread(picture, cv2.IMREAD_GRAYSCALE)
cv2.imwrite('Gray.jpg', bw)
cv2.imshow('Imagen en escala de Grises', bw)
cv2.waitKey(0)

#Matplotlib with OpenCV BGR
img = cv2.imread(picture, -1)
plt.imshow(img, cmap= 'gray', interpolation = 'bicubic')
plt.title('BGR')
plt.xticks([]), plt.yticks([])
plt.show()

#Matplotlib RGB
img=mpimg.imread(picture)
imgplot = plt.imshow(img,  cmap= 'gray', interpolation = 'bicubic')
plt.title('RGB')
plt.xticks([]), plt.yticks([])
plt.show()


