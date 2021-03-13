# Problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Score: 10.0


a = input()
set_a = set(input().split())
b = input()
set_b = set(input().split())
print(len(set_a ^ set_b))
