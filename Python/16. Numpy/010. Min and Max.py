# Problem: https://www.hackerrank.com/challenges/np-min-and-max/problem
# Score: 20.0


import numpy as np

n,m = map(int, input().split())
my_array = np.array([input().strip().split() for _ in range(n)], int)
print(np.max(np.min(my_array, axis = 1)))
