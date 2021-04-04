# Problem: https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# Score: 20.0


import numpy as np

n,m = map(int, input().split())
my_array = np.array([input().strip().split() for _ in range(n)], int)
print(np.prod(np.sum(my_array, axis=0), axis=0))
