#Works well on Jupyter NoteBook. Effects applied by code blocks
import cv2
import matplotlib.pyplot as plt
import numpy as np

#Funcion para mostrar las imagenes en Jupyter NoteBook
def display_image(img, cmap=None):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)

#Mostrar la imagen en RGB
img = cv2.imread(input('Introduce la ruta de la imagen y su extension'))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
display_image(img)

#----------------------------------------------------------Filtros Binarios
ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
display_image(thresh1)

img = cv2.imread(input('Introduce la ruta de la imagen y su extension: '),0)
ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
display_image(thresh1)


img = cv2.imread(input('Introduce la ruta de la imagen y su extension: '))
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
display_image(img)

#-------------------------------------------------------Filtro kernel numpy
kernel = np.ones(shape=(4,4), dtype=np.float32)/10
kernel
img = cv2.imread(input('Introduce la ruta de la imagen y su extension: '))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
result = cv2.filter2D(img,-1,kernel)
display_image(result)

img = cv2.imread(input('Introduce la ruta de la imagen y su extension: '),0)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
display_image(sobelx)
#display_image(sobelx,cmap='gray') Metallic effect

#-------------------------------------------------------Mostrar Histograma
img = cv2.imread(input('Introduce la ruta de la imagen y su extension: '))
color = ['b','g','r']
for i, col in enumerate(color):
    histr = cv2.calcHist([img],[i], None,[256],[0,256])
    plt.plot(histr,color=col)
plt.title('Histograma')

