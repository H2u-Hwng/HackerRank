# Problem: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# Score: 20.0


import numpy

n, m = map(int, input().strip().split(' '))
my_array = numpy.array([input().strip().split(' ') for _ in range(n)], int) 
print(my_array.transpose())
print(my_array.flatten())
