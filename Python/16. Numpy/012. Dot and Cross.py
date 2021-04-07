# Problem: https://www.hackerrank.com/challenges/np-dot-and-cross/problem
# Score: 20.0


import numpy as np

n = int(input())
arr_a = np.array([input().strip().split() for _ in range(n)], int)
arr_b = np.array([input().strip().split() for _ in range(n)], int)
print(np.dot(arr_a,arr_b))
