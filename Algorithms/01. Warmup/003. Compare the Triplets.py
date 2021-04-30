# Problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Score: 10.0


import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    score = [0,0]
    for i in range(len(a)):
        score[0] += a[i] > b[i]
        score[1] += a[i] < b[i]
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
