#!/user/bin/env python3
import numpy as np


my_list = [1, 2, 3]
print(type(my_list))
print('-'*50)
my_array = np.array(my_list)
print(my_array)
print('-'*50)
print(type(my_array))
print('-'*50)
print(np.arange(0, 10, 2))
print('-'*50)
print(np.zeros(shape=(10, 5)))
print('-'*50)
print(np.ones(shape=(2, 4)))
print('-'*50)
####################################
# NUMPY RANDOM
####################################
np.random.seed(101)
arr = np.random.randint(0, 100, 10)
print(arr)
print('-'*50)
arr2 = np.random.randint(0, 100, 10)
print(arr2)
print('-'*50)
print(arr.max())
print(arr2.max())
print('-'*50)
print(arr.argmax())
print(arr2.argmax())
print('-'*50)
print(arr.min())
print(arr2.min())
print('-'*50)
print(arr.argmin())
print(arr2.argmin())
print('-'*50)
print(arr.mean())
print(arr2.mean())
print('-'*50)
print(arr.shape)
print(arr2.shape)
print('-'*50)
print(arr.reshape(2, 5))
print('-'*50)
print(arr2.reshape(5, 2))
print('-'*50)
####################################
# NUMPY INDEXING
####################################
mat = np.arange(0, 100).reshape(10, 10)
print(mat)
print('-'*50)
print(mat.shape)
print('-'*50)
row = 0
col = 1
print(mat[row, col])
print(mat[4, 6])
print('-'*50)
print(mat[:, 1])
