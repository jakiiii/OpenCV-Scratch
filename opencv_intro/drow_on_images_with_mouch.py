#!/bin/user/eve python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython, display
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')


# Functions
def draw_circle(event, x, y, flags, prams):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


cv2.namedWindow(winname='new_img')
cv2.setMouseCallback('new_img', draw_circle)


# Sowing Image with OpenCV
# img = np.zeros((512, 512, 3), np.int8)
img = cv2.imread('../images/gray.jpg')

while True:
    cv2.imshow('new_img', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
