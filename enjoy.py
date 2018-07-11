#!/usr/bin/env python3

import keras
import cv2
import numpy as np

class Enjoy:
    # FRAME_COORDS = ((350,100), (650,400))
    FRAME_COORDS = ((350,100), (600,350))
    TAGS = ['rock', 'paper','scissors']

    def __init__(self, filePath):
        self.model = keras.models.load_model(filePath)

        self.cap = cv2.VideoCapture(0)
        self.capture()
    
    def capture(self):
        while True:
            ret, frame = self.cap.read()

            frame = cv2.flip(frame, 1)
            frame = cv2.rectangle(frame, *self.FRAME_COORDS, (255,0,0), 2)

            cropped = frame[
                self.FRAME_COORDS[0][1] + 2 : self.FRAME_COORDS[1][1] - 1,
                self.FRAME_COORDS[0][0] + 2 : self.FRAME_COORDS[1][0] - 1
            ]
            hand = cv2.resize(cropped, (150, 150))
            predictedTag = self.identify(hand)

            self.write(frame)
            cv2.imshow("frame", frame)
            
            key = cv2.waitKey(1)    
            if key & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()

    def identify(img):
        print (self.model.predict(img) )


    def write(self, img):
        cv2.putText(img, self.TAGS[self.tagIdx],
            (self.FRAME_COORDS[0][0], self.FRAME_COORDS[0][1] - 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)

    def nextTag(self):
        self.tagIdx = (self.tagIdx + 1) % 3

if __name__ == "__main__":
    test = Enjoy('first_try.h5')
