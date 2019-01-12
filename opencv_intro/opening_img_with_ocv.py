#!/bin/user/evn python3
import cv2


img = cv2.imread('../images/shahid.jpg')

while True:
    cv2.imshow('Shahed Afridi', img)

    # If we'he waited at least 1 ms AND we've press Esc key.
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
