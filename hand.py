# coding: utf-8


# import matplotlib.pyplot as plt
# img = cv2.imread("images/hand1.jpg", cv2.IMREAD_GRAYSCALE) 
# plt.imshow(img, cmap="gray", interpolation="bicubic")
# plt.show()



import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
hand_cascade = cv2.CascadeClassifier('hand.xml')

cap = cv2.VideoCapture(0)

def draw_rectangle(frame, gray, coors):
    for (x,y,w,h) in coors:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    return frame

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)

    frame = draw_rectangle(frame, gray, faces)
    # frame = draw_rectangle(frame, gray, hands)
    
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cv2.destroyAllWindows()
