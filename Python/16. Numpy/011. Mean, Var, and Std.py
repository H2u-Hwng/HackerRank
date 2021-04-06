# Problem: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
# Score: 20.0


import numpy as np

n,m = map(int, input().split())
my_array = np.array([input().strip().split() for _ in range(n)], int)
print(np.mean(my_array, axis=1), np.var(my_array, axis=0), np.around(np.std(my_array), decimals=11), sep='\n')
