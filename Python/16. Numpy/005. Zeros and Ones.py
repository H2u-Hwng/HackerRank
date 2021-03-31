# Problem: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
# Score: 20.0


import numpy

nums = tuple(map(int, input().split(' ')))
print(numpy.zeros(nums, dtype = numpy.int))
print(numpy.ones(nums, dtype = numpy.int))
