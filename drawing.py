import cv2
import numpy as np
from math import sqrt
from tkinter import colorchooser

mode = 'circle'
colorXo = colorchooser.askcolor()
R = colorXo[0][0]
G = colorXo[0][1]
B = colorXo[0][2]
color = (B,G,R)
pt = None
tk=1

def on_track(value):
    global tk
    
    # el valor -1 dibuja una figura rellena
    tk = -1 if value == 0 else value

    # no se puede rellenar una line
    if mode == 'line' and tk == -1:
        tk = 1

def on_mouse(event, x, y, flags, param):

    global pt, draw

    if event == cv2.EVENT_LBUTTONDOWN:
        pt = (x, y)
        print('Dibujando ', mode, ', en el punto: ', pt)
        
    elif event == cv2.EVENT_LBUTTONUP:
        
        if mode == 'circle':  
            rad = sqrt(pow(pt[0] - x, 2) + pow(pt[1] - y, 2))
            cv2.circle(param, pt, int(rad), color, tk, cv2.LINE_AA)
            
        elif mode == 'rectangle':
            cv2.rectangle(param, pt, (x, y), color, tk, cv2.LINE_AA)
            
        elif mode == 'line':
            cv2.line(param, pt, (x, y), color, tk, cv2.LINE_AA)


if __name__ == "__main__":

    title = 'Drawing'
    image = np.zeros((600, 800, 3), np.uint8)
    
    cv2.namedWindow(title)
    cv2.createTrackbar('RELLENO', title, 1, 10, on_track)
    cv2.setMouseCallback(title, on_mouse, image)
    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(image, 'Icarpio', (0,560), font, 1 , (255,255,255), 1, cv2.LINE_AA)

    while(1):
        cv2.imshow(title, image)
        key = cv2.waitKey(20) & 0xFF
        
        if key == ord('c'):
            mode = 'circle'
        elif key == ord('r'):
            mode = 'rectangle'
        elif key == ord('l'):
            mode = 'line'
        elif key == 27:
            break
        
    cv2.destroyAllWindows()