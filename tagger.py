import cv2

cap = cv2.VideoCapture(0)

DEST_FOLDER = './img/'
FRAME_COORDS = ((355,100),(600,400))

def gen_count():
    count = 0
    while True:
        yield count
        count += 1

def save_frame(frame, gesture):
    """
    Saves the frame to the DEST_FOLDER

    :param frame: A frame from a video feed
    :param gesture: The hand gesture shown (rock | paper | scissor | bird)
    """

    count = next(gen_count())
    print(count)
    cv2.imwrite(DEST_FOLDER + gesture + '/' + str(count) + '.png', frame)

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame = cv2.rectangle(frame, *FRAME_COORDS, (255,0,0), 2)

    cropped = frame[
        FRAME_COORDS[0][1]+2:FRAME_COORDS[1][1]-1,
        FRAME_COORDS[0][0]+2:FRAME_COORDS[1][0]-1
    ]

    save_frame(cropped, 'rock')

    cv2.imshow("img", frame)
    
    # commands
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break    

cv2.destroyAllWindows()

