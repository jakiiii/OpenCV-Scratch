#!user/bin/env python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')


cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# TOP LEFT Corner
x = width // 2
y = height // 2

# width and height of RECTANGLE
w = width // 4
h = height // 4

# Bottom Right Corner x + w, y + h

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=4)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
