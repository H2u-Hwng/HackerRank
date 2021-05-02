# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Score: 10.0


import math
import os
import random
import re
import sys

def diagonalDifference(arr,n):
    d1 = 0
    d2 = 0
    for i in range(n):
        d1 += arr[i][i]
        d2 += arr[i][n-i-1]   
    return abs(d1-d2)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
