# Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Score: 10.0


k = int(input())
arr = list(map(int, input().split()))
s = set(arr)
result = (sum(s)*k - sum(arr))//(k-1)
print(result)
