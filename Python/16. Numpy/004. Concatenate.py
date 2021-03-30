# Problem: https://www.hackerrank.com/challenges/np-concatenate/problem
# Score: 20.0


import numpy

n,m,p = map(int, input().split(' '))
arr_n = numpy.array([input().strip().split(' ') for _ in range(n)], int)
arr_m = numpy.array([input().strip().split(' ') for _ in range(m)], int)
print(numpy.concatenate((arr_n, arr_m), axis = 0))
