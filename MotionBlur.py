# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:22 2019

@author: ICarpio
"""

#EFFECTS

import cv2
import numpy as np
import math

img = cv2.imread('rosalia.jpg')

#Motion Blur
size = 15
#Generamos el kernel
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size
#Aplicamos el kernel a la imagen
output = cv2.filter2D(img, -1, kernel_motion_blur)
cv2.imshow('Motion Blur', output)


img = cv2.imread('rosalia.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

#Vertical Wave
output = np.zeros(img.shape, dtype=img.dtype)
for i in range(rows):
    for j in range(cols):
        offset_x = int(50.0 * math.sin(2 * 3.14 * i / 180))
        offset_y = 0
        if j+offset_x < rows:
            output[i,j] = img[i,(j+offset_x)%cols]
        else:
            output[i,j] = 0
            
cv2.imshow('Vertical Wave', output)

#Horizontal wave
output = np.zeros(img.shape, dtype=img.dtype)
for i in range(rows):
    for j in range(cols):
        offset_x = 0
        offset_y = int(16.0 * math.sin(2 * 3.14 * j / 150))
        if i+offset_y < rows:
            output[i,j] = img[(i+offset_y)%rows,j]
        else:
            output[i,j] = 0
cv2.imshow('Horizontal wave', output)

#Multidirectional Wave
output = np.zeros(img.shape, dtype=img.dtype)
for i in range(rows):
    for j in range(cols):
        offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
        offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
        if i+offset_y < rows and j+offset_x < cols:
            output[i,j] = img[(i+offset_y)%rows,(j+offset_x)%cols]
        else:
            output[i,j] = 0
            
cv2.imshow('Multidirectional Wave', output)

#Concave effect
output = np.zeros(img.shape, dtype=img.dtype)
for i in range(rows):
    for j in range(cols):
        offset_x = int(130.0 * math.sin(2 * 3.14 * i / (2*cols)))
        offset_y = 0
        if offset_x < cols:
             output[i,j] = img[i,(j+offset_x)%cols]
        else:
            output[i,j] = 0
            
cv2.imshow('Concave effect', output)       
cv2.waitKey(0)
cv2.destroyAllWindows()
