import cv2

class Tagger:
    DEST_FOLDER = './testdata/'
    FRAME_COORDS = ((355,100), (700,500))
    TAGS = ['rock', 'paper','scissors']

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.tagIdx = 0
        self.count = 0
    
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

    def capture(self):
        while True:
            ret, frame = self.cap.read()

            frame = cv2.flip(frame, 1)
            frame = cv2.rectangle(frame, *self.FRAME_COORDS, (255,0,0), 2)

            cropped = frame[
                self.FRAME_COORDS[0][1] + 2 : self.FRAME_COORDS[1][1] - 1,
                self.FRAME_COORDS[0][0] + 2 : self.FRAME_COORDS[1][0] - 1
            ]

            self.write(frame)
            cv2.imshow("img", frame)
            
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
            (self.FRAME_COORDS[0][0] - 100, self.FRAME_COORDS[0][1] + 300),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)

        cv2.putText(img, "Press [t] to change tag",
            (self.FRAME_COORDS[0][0] - 100, self.FRAME_COORDS[0][1] + 340),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)

        cv2.putText(img, self.TAGS[self.tagIdx],
            (self.FRAME_COORDS[0][0], self.FRAME_COORDS[0][1] - 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)

if __name__ == "__main__":
    test = Tagger()
    test.capture()