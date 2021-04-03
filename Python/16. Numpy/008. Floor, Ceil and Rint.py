# Problem: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
# Score: 20.0


import numpy as np

np.set_printoptions(legacy ='1.13')
a = np.array(input().strip().split(), float)
print(np.floor(a), np.ceil(a), np.rint(a), sep='\n')
