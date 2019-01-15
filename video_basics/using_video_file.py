#!user/bin/env python3
import cv2
import time


cap = cv2.VideoCapture('../videos/first_video.mp4')

if cap.isOpened() == False:
    print('Error, File Not Found!')

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # Writer 25 FPS
        time.sleep(1/25)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
