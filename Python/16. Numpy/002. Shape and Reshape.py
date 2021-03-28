# Problem: https://www.hackerrank.com/challenges/np-shape-reshape/problem
# Score: 20.0


import numpy

arr = numpy.array(input().strip().split(' '), int)
print(arr.reshape(3,3))
