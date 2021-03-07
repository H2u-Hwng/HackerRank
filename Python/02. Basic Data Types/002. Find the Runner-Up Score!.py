# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Score: 10.0


n = int(input())
A = list(map(int,input().strip().split()))[:n]
i = max(A)
while max(A) == i:
    A.remove(max(A))
print(max(A))
