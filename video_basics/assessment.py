#!/bin/user/env python3
import cv2


center = (0, 0)
clicked = False


def draw_circle(event, x, y, flags, prams):
    global center, clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        clicked = False

    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cv2.namedWindow('Video Frame')
cv2.setMouseCallback('Video Frame', draw_circle)

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    if clicked:
        cv2.circle(frame, center=center, radius=50, color=(255, 0, 0), thickness=4)

    cv2.imshow('Video Frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
