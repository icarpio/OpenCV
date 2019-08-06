# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:01 2019

@author: Icarpio
"""

import cv2
import numpy as np

width = 400
height = 300
dim = (width, height)
# resize image

original = cv2.imread(input('Introduce la ruta de la imagen y su extension'))
resized = cv2.resize(original, dim, interpolation = cv2.INTER_AREA)
#Vertical
flipVer = cv2.flip(resized, 0)
#Horizontal
flipHor = cv2.flip(resized, 1)
#Flip Both Image
flipBoth = cv2.flip(resized, -1)


cv2.imshow('Original', resized)
cv2.imshow('Flip Vertical', flipVer)
#cv2.imshow('Flip Horizontal', flipHor)
cv2.imshow('Flip Both Image ', flipBoth)


rows, cols = resized.shape[:2]
src_points = np.float32([[0,0], [cols-1,0],[0,rows-1]])
dst_points = np.float32([[cols-1,0], [0,0],[cols-1,rows-1]])
matrix = cv2.getAffineTransform(src_points, dst_points)
mirror = cv2.warpAffine(resized, matrix, (cols,rows))
cv2.imshow('Mirror', mirror)

cv2.waitKey(0)
cv2.destroyAllWindows()