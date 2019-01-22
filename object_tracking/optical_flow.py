#!/user/bin/ven python
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')


corner_track_prams = dict(maxCorners=10, qualityLevel=0.3, minDistance=7, blockSize=7)
lk_prams = dict(winSize=(200, 200), maxLevel=2,  criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# PTS TO TRACK
prevPts = cv2.goodFeaturesToTrack(prev_gray, mask=None, **corner_track_prams)
mask = np.zeros_like(prev_frame)

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, frame_gray, prevPts, None, **lk_prams)

    good_new = nextPts[status == 1]
    good_prev = prevPts[status == 1]

    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()
        mask = cv2.line(mask, (x_new, y_new), (x_prev, y_prev), (0, 255, 0), 3)
        frame = cv2.circle(frame, (x_new, y_new), 8, (0, 0, 255), -1)

    img = cv2.add(frame, mask)
    cv2.imshow('tracking', img)

    if cv2.waitKey(30) & 0xFF == 27:
        break

prev_gray = frame_gray.copy()
prevPts = good_new.reshape(-1, 1, 2)

cap.release()
cv2.destroyAllWindows()
