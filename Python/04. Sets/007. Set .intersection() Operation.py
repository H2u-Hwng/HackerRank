# Problem: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Score: 10.0


n = int(input())
set_n = set(input().split())
b = int(input())
set_b = set(input().split())
print(len(set_n & set_b))
