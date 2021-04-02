# Problem: https://www.hackerrank.com/challenges/np-array-mathematics/problem
# Score: 20.0


import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
