# Problem: https://www.hackerrank.com/challenges/30-arrays/problem
# Score: 30.0


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(*arr[::-1])
