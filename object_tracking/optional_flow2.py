#!/user/bin/ven python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')


cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
prev_img = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

hsv_musk = np.zeros_like(frame1)
hsv_musk[:, :, 1] = 255

while True:
    ret, frame2 = cap.read()
    next_img = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prev_img, next_img, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(flow[:, :, 0], flow[:, :, 1], angleInDegrees=True)
    hsv_musk[:, :, 0] = ang/2
    hsv_musk[:, :, 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv_musk, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame', bgr)

    if cv2.waitKey(10) & 0xFF == 27:
        break

    prev_img = next_img

cap.release()
cv2.destroyAllWindows()
