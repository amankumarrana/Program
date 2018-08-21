# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:02:39 2018

@author: baman
"""

import numpy as np
arr_val = np.array([8, 8, 3, 7, 7, 0, 4, 2, 5, 2])
print("Array", arr_val)

# position where value > 5

index_of_5 = np.where(arr_val > 5)
print("positions where value > 5 " ,index_of_5)
print("Value greater than 5 ", np.take(arr_val, index_of_5))

print(np.where(arr_val > 5, 'ge5', 'le5'))
print("Max value of an array", arr_val[np.argmax(arr_val)])

np.set_printoptions(suppress=True)
path = 'https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv'
data = np.genfromtxt(path, delimiter=',', skip_header=1, filling_values=-999, dtype=None)
np.save('auto', data)
dd = np.load('auto.npy')

zeros = np.zeros([2,3])
ones = np.ones([2,3])
print(np.concatenate([zeros, ones], axis =0))
