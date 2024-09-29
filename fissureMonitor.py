import cv2
import numpy as np

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    _, frame = cap.read()

    frame = frame[0:350, 15:540] #tirando a borda da imagem

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converter imagem em tons de cinza

    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    #dilatação para a imagem ficar um pouco maior
    kernel = np.ones((5,5),np.uint8)

    dilation = cv2.erode(threshold,kernel,iterations = 1)

    contours,_ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for (i,c) in enumerate(contours):
        (x,y,w,h) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        #aferir altura
        cmY = (h*10)/260
        cv2.putText(frame, str(float(cmY)), (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)
        #cv2.putText(frame, str(h), (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)
        
        #aferir largura
        #cmX = (w*10)/71 #regra de três
        #cv2.putText(frame, str(int(cmX)), (x+w+15, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1) 
        

    cv2.imshow("Monitor de Fissuras - AP|RAC v1.0", frame)
    #cv2.imshow("Gray", gray)
    #cv2.imshow("Threshold", threshold)
    cv2.imshow("Dilatation", dilation)



    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()