"""
Export a series of tagged images to a specified directory, from a timed video capture

:return: list of tagged filenames

>>> e = RPS()
>>> e.start_capture()
Starting capture...
"""

import cv2

class RPS:
    # Area to which images will be cropped
    CROP = ((355,100), (600,400), (300, 0, 0)) 

    def __init__(self, webcam=0):
        self.images = []
        self.webcam = webcam
        self.dest_folder = './testdata/'

    def start_training(self):
        cap = cv2.VideoCapture(self.webcam)
        print("Starting capture...")
        
        while True:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.rectangle(frame, *self.CROP, 2)

            cropped = frame[
                self.CROP[0][1] + 2 : self.CROP[1][1] - 1,
                self.CROP[0][0] + 2 : self.CROP[1][0] - 1
            ]

            cv2.imshow("img", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()

if __name__ == "__main__":
    import doctest
    doctest.testmod()