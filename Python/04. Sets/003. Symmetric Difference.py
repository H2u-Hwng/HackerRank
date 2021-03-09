# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Score: 10.0


_ = input()
m = set(input().split())
_ = input()
n = set(input().split())
result = (m.difference(n)).union(n.difference(m))
print("\n".join(sorted(result, key=int)))
