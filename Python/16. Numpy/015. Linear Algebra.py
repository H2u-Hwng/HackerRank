# Problem: https://www.hackerrank.com/challenges/np-linear-algebra/problem
# Score: 20.0


import numpy as np

n = int(input())
a = np.array([input().strip().split() for _ in range(n)], float)
print(round(np.linalg.det(a), 2))
