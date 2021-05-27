# Problem: https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# Score: 30.0


import numpy as np

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(max(sorted(numbers), key=numbers.count))
