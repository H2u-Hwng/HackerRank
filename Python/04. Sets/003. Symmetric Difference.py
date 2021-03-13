# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Score: 10.0


m = int(input())
set_m = set(input().split())
n = int(input())
set_n = set(input().split())
print('\n'.join(sorted(set_m ^ set_n, key = int)))
