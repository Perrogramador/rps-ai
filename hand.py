# coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/hand1.jpg", cv2.IMREAD_GRAYSCALE) 

plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.show()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    
    cv2.imshow("img", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cv2.destroyAllWindows()

