#!/bin/user/env python3
import cv2
import numpy as np
from matplotlib import cm
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')


road = cv2.imread('../images/image_road.jpg')
road_copy = np.copy(road)
marker_image = np.zeros(road.shape[:2], dtype=np.int32)
segments = np.zeros(road.shape, dtype=np.uint8)


def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)


colors = []
for i in range(10):
    colors.append(create_rgb(i))

# GLOBAL VARIABLES
# COLOR CHOICE
n_markers = 10  # [0 to 9]
current_marker = 1
# MARKERS UPDATED BY WATERSHED
marks_updated = False


# CALLBACK Function
def mouse_callback(event, x, y, flags, param):
    global marks_updated
    if event == cv2.EVENT_LBUTTONDOWN:
        # MARKERS PASSED TO THE WATERSHED ALGORITHM
        cv2.circle(marker_image, (x, y), 10, current_marker, -1)
        # USER SEES ON THE ROAD IMAGE
        cv2.circle(road_copy, (x, y), 10, colors[current_marker], -1)

        marks_updated = True


cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)


# LOOP
while True:
    cv2.imshow('Watershed Segments', segments)
    cv2.imshow('Road Image', road_copy)

    # CLOSE ALL WINDOW
    k = cv2.waitKey(1)
    if k == 27:
        break
    # CLEARING ALL THE COLORS PRESS C KEY
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)
        segments = np.zeros(road.shape, dtype=np.uint8)
    # UPDATE COLOR CHOICE
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))

    # UPDATE THE MARKING
    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)

        segments = np.zeros(road.shape, dtype=np.uint8)
        for color_index in range(n_markers):
            # COLORING SEGMENTS, NUMPY CALL
            segments[marker_image_copy == color_index] = colors[color_index]

cv2.destroyAllWindows()
