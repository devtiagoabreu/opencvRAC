import cv2
import numpy as np

windowName = "Projeto RAC - Monitor de Fissuras v1.0"

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
  print("não abriu")
  exit()

while True:
  ret, frame = cap.read()

  if not ret:
    print("não tem frame")
    break

  frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)



  kernel = np.ones((5,5),np.uint8)

  dilation = cv2.erode(frame,kernel,iterations = 1)

  contours,_ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


  for (i,c) in enumerate(contours):
      (x,y,w,h) = cv2.boundingRect(c)
      area = cv2.contourArea(c)
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
      cmY = (h*15)/120
      cmX = (w*10)/71
      cv2.putText(frame, str(int(cmY)), (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)
      cv2.putText(frame, str(int(cmX)), (x+w+15, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)





  cv2.imshow(windowName, frame)

  k = cv2.waitKey(1)

  if k == ord('q'):
    break

  if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
    break

  cv2.destroyAllWindows()
  cap.release()
  print("Encerrou")