import cv2

#Captura de video
def record():
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter('videoOut.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0,(640,480))
    while(cap.isOpened()):
        ret, img = cap.read()
        if ret == True:
            cv2.imshow('Video', img)
            out.write(img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


#Mostrar el video
def show():
    cap = cv2.VideoCapture('videoOut.avi')
    while(cap.isOpened()):
        ret, img = cap.read()
        if ret == True:
            cv2.imshow('Video', img)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        else:break
    cap.release()
    cv2.destroyAllWindows()


 
switcher = {
        1: record,
        2: show
    }
 
 
def switch(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument)
    # Execute the function
    return func()

case = int(input("Pulse 1 para grabar o 2 para mostrar el video ya guardado: "))
switch(case)


    

