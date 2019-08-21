# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:29 2019

@author: Icarpio
"""


import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

if face_cascade.empty():
	raise IOError('Unable to load the face cascade classifier xml file')

if eye_cascade.empty():
	raise IOError('Unable to load the eye cascade classifier xml file')
    
img = cv2.imread('cara.jpg')
sunglasses_img = cv2.imread('eyes.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
centers = []
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(roi_gray)
	for (x_eye,y_eye,w_eye,h_eye) in eyes:
		centers.append((x + int(x_eye + 0.5*w_eye), y + int(y_eye + 0.5*h_eye)))
# Overlay sunglasses; the factor 2.12 is customizable depending on the size of the face
if len(centers) > 0:
	sunglasses_width = 2.12 * abs(centers[1][0] - centers[0][0])
	overlay_img = np.ones(img.shape, np.uint8) * 255
	h, w = sunglasses_img.shape[:2]
	scaling_factor = sunglasses_width / w
	overlay_sunglasses = cv2.resize(sunglasses_img, None,fx=scaling_factor,fy=scaling_factor, interpolation=cv2.INTER_AREA)
	x = centers[0][0] if centers[0][0] < centers[1][0] else centers[1][0]

	# customizable X and Y locations; depends on the size of the face
	x -= 0.26*overlay_sunglasses.shape[1]
	y += 0.85*overlay_sunglasses.shape[0]
	h, w = overlay_sunglasses.shape[:2]
	overlay_img[y:y+h, x:x+w] = overlay_sunglasses

	# Create mask
	gray_sunglasses = cv2.cvtColor(overlay_img, cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(gray_sunglasses, 110, 255, cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)
	temp = cv2.bitwise_and(img, img, mask=mask)
	temp2 = cv2.bitwise_and(overlay_img, overlay_img, mask=mask_inv)
	final_img = cv2.add(temp, temp2)
	cv2.imshow('Eye Detector', img)
	cv2.imshow('Sunglasses', final_img)
	cv2.waitKey()
	cv2.destroyAllWindows()

