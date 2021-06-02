# Problem: https://www.hackerrank.com/challenges/s10-standard-deviation/problem
# Score: 30.0


from statistics import pstdev

n = int(input().strip())
vals = list(map(int, input().rstrip().split()))

print(round(pstdev(vals),1))
