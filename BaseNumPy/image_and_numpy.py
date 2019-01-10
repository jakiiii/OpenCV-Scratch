#!/bin/user/eve python3
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

pic = Image.open('../images/mas.jpg')
print(pic)
print(type(pic))
print('-'*50)
pic_arr = np.asarray(pic)
print(type(pic_arr))
print('-'*50)
print(pic_arr.shape)
print(plt.imshow(pic_arr))
print('-'*50)
pic_red = pic_arr.copy()
print(plt.imshow(pic_red))
print('-'*50)
print(pic_red.shape)
print(pic_red[:, :, 0])
print('-'*50)
print(plt.imshow(pic_red[:, :, 0]))
print('-'*50)
print(plt.imshow(pic_red[:, :, 0], cmap='gray'))
