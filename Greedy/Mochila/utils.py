'''
Created on 14 ago. 2021

@author: Lenovo
'''
import numpy as np
from mochila_greddy import ratio
val= np.array([2,6,8,7,3,4,6,5,10,9,8,11,12,15,6,8,13,14,15,16,13,14,15,26,13,9,25,26])
pes = np.array([7,3,3,5,4,7,5,4,15,10,17,3,6,11,6,14,4,8,9,10,14,17,9,24,11,17,12,14])
W_capacity = 30

print(sorted(ratio(val,pes)))