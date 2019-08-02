# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:28:26 2019

@author: Yvan
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def resized(picture):
    img = cv2.imread(picture, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape)
    width = 450
    height = 550
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized.shape)
    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
resized('vacas.jpg')
resized('stranger.jpg')
resized('char.jpg')