import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython, display

ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

img = np.zeros((512, 512, 3), np.int8)
# img = cv2.imread('../images/gray.jpg')
print(plt.imshow(img))
while True:
    cv2.imshow('NewImage', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
