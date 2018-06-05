import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    frame = cv2.rectangle(frame,(355,100),(600,400),(255,0,0),2)
    
    cv2.imshow("img", frame)
    
    # commands
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break    

cv2.destroyAllWindows()