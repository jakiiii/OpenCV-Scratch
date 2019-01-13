import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython, display
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')


# Variables
drawing = False
ix, iy = -1, -1


# Function description
def draw_rectangle(event, x, y, flags, prams):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


# Function call
cv2.namedWindow(winname='draw_rectangle')
cv2.setMouseCallback('draw_rectangle', draw_rectangle)

# Showing the images
# img = np.zeros((512, 512, 3))
img = cv2.imread('D:\Dev\OpenCV\images\gray.jpg')
while True:
    cv2.imshow('draw_rectangle', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
