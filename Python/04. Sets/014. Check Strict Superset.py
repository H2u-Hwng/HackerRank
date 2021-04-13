# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Score: 10.0


a = set(input().strip().split())
nums = int(input())
count = 0
for _ in range(nums):
    n = set(input().strip().split())
    if a.issuperset(n):
        count += 1
print(count == nums)
