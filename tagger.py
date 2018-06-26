#!/usr/bin/env python3

import cv2
import numpy as np

class Tagger:
    DEST_FOLDER = './testdata/'
    FRAME_COORDS = ((355,100), (700,500))
    TAGS = ['rock', 'paper','scissors']

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.tagIdx = 0
        self.count = 0
        self.h = 99
        self.s = 41
        self.v = 156
        self.H = 115
        self.S = 141
        self.V = 255

        self.capture()
    
    def nextTag(self):
        self.tagIdx = (self.tagIdx + 1) % 3

    def saveFrame(self, frame):
        """
        Saves the frame to the DEST_FOLDER

        :param frame: A frame from a video feed
        :param gesture: The hand gesture shown (rock | paper | scissor | bird)
        """

        self.count += 1
        cv2.imwrite(self.DEST_FOLDER + self.TAGS[self.tagIdx] + '/' + str(self.count) + '.png', frame)
        print(self.count)

    def set_h(self, n):
        self.h = n
    def set_s(self, n):
        self.s = n
    def set_v(self, n):
        self.v = n
    def set_H(self, n):
        self.H = n
    def set_S(self, n):
        self.S = n
    def set_V(self, n):
        self.V = n

    def capture(self):
        while True:
            ret, frame = self.cap.read()

            frame = cv2.flip(frame, 1)
            frame = cv2.rectangle(frame, *self.FRAME_COORDS, (255,0,0), 2)

            # Convert frame to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            lower_blue = np.array([self.h, self.s, self.v])
            upper_blue = np.array([self.H, self.S, self.V])


            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            res = cv2.bitwise_and(frame, frame, mask= mask)

            cropped = hsv[
                self.FRAME_COORDS[0][1] + 2 : self.FRAME_COORDS[1][1] - 1,
                self.FRAME_COORDS[0][0] + 2 : self.FRAME_COORDS[1][0] - 1
            ]

            self.write(hsv)
            #cv2.imshow("frame", frame)
            cv2.imshow("hsv", hsv)
            # cv2.imshow("mask", mask)
            # cv2.imshow("res", res)
            cv2.createTrackbar("h", "hsv", 0, 255, self.set_h)
            cv2.createTrackbar("s", "hsv", 0, 255, self.set_s)
            cv2.createTrackbar("v", "hsv", 0, 255, self.set_v)
            cv2.createTrackbar("H", "hsv", 0, 255, self.set_H)
            cv2.createTrackbar("S", "hsv", 0, 255, self.set_S)
            cv2.createTrackbar("V", "hsv", 0, 255, self.set_V)
            
            
            key = cv2.waitKey(1)    
            # commands
            if key & 0xFF == ord("q"):
                break
            if key & 0xFF == ord("s"):
                self.saveFrame(cropped)
            if key & 0xFF == ord("t"):
                self.nextTag()
                

        cv2.destroyAllWindows()

    def write(self, img):
        cv2.putText(img, "Press [s] to toggle recording",
            (self.FRAME_COORDS[0][0] - 800, self.FRAME_COORDS[0][1] + 500),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)

        cv2.putText(img, "Press [t] to change tag",
            (self.FRAME_COORDS[0][0] - 80, self.FRAME_COORDS[0][1] + 540),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)

        cv2.putText(img, self.TAGS[self.tagIdx],
            (self.FRAME_COORDS[0][0], self.FRAME_COORDS[0][1] - 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)


if __name__ == "__main__":
    test = Tagger()
