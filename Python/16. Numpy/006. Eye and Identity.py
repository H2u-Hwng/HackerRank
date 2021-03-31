# Problem: https://www.hackerrank.com/challenges/np-eye-and-identity/problem
# Score: 20.0


import numpy

n, m = map(int, input().split(' '))
numpy.set_printoptions(legacy = '1.13')
print(numpy.eye(n, m))
