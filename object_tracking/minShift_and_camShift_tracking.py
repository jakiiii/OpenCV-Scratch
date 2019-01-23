#!/user/bin/ven python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')


cap = cv2.VideoCapture(0)
ret, frame = cap.read()
face_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
face_rect = face_cascade.detectMultiScale(frame)

(face_x, face_y, w, h) = tuple(face_rect[0])
track_window = (face_x, face_y, w, h)
roi = frame[face_y:face_y+h, face_x:face_x+w]

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
term_criteria = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ##############################
        # ret, track_window = cv2.meanShift(dst, track_window, term_criteria)
        # x, y, w, h = track_window
        # img2 = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
        ##############################
        ret, track_window = cv2.CamShift(dst, track_window, term_criteria)
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame, [pts], True, (0, 0, 255), 2)

        cv2.imshow('img', img2)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break


cv2.destroyAllWindows()
cap.release()
