# Problem: https://www.hackerrank.com/challenges/py-check-subset/problem
# Score: 10.0


t = int(input())
for _ in range(t):
    nums_a = int(input())
    a = set(input().strip().split())
    nums_b = int(input())
    b = set(input().strip().split())
    print(a.issubset(b))
