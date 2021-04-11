# Problem: https://www.hackerrank.com/challenges/no-idea/problem
# Score: 50.0


n,m = map(int, input().split())
nums = input().split()
a = set(input().strip().split())
b = set(input().strip().split())
print(sum([(i in a) - (i in b) for i in nums]))
