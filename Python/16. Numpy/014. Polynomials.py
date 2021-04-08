# Problem: https://www.hackerrank.com/challenges/np-polynomials/problem
# Score: 20.0


import numpy as np

p = np.array(input().strip().split(),float)
x = int(input())
print(np.polyval(p,x))
