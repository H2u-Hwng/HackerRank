# Problem: https://www.hackerrank.com/challenges/np-inner-and-outer/problem
# Score: 20.0


import numpy as np

A = np.array(input().strip().split(), int)
B = np.array(input().strip().split(), int)
print(np.inner(A,B), np.outer(A,B), sep='\n')
