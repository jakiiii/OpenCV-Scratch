#!user/bin/env python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')


# GLOBAL VARIABLES
pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
botRight_clicked = False


# CALLBACK FUNCTION RECTANGLE
def draw_rectangle(event, x, y, flags, prams):
    global pt1, pt2, topLeft_clicked, botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        # RESET RECTANGLE
        if topLeft_clicked == True and botRight_clicked == True:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeft_clicked = False
            botRight_clicked = False

        if topLeft_clicked == False:
            pt1 = (x, y)
            topLeft_clicked = True
        elif botRight_clicked == False:
            pt2 = (x, y)
            botRight_clicked = True


cv2.namedWindow('Testing Draw')
cv2.setMouseCallback('Testing Draw', draw_rectangle)

# CONNECT TO THE CALLBACK
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # DRAWING ON THE FRAME BASED OF THE GLOBAL VARIABLES
    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)

    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)

    cv2.imshow('Testing Draw', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
