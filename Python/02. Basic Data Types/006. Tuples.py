# Problem: https://www.hackerrank.com/challenges/python-tuples/problem
# Score: 10.0


n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))
