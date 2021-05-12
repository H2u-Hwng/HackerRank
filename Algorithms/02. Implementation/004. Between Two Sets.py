# Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
# Score: 10.0


from math import gcd
from functools import reduce

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))

def LCM(a, b):
    return (a*b)//gcd(a,b)

lcm = reduce(LCM, arr)
gcd = reduce(gcd, brr)

lcm_copy = lcm
count = 0
while lcm <= gcd:
    if(gcd % lcm) == 0:
        count += 1
    lcm = lcm + lcm_copy

print(count)
