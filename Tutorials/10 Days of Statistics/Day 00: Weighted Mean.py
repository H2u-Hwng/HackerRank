# Problem: https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# Score: 30.0


n = int(input().strip())
vals = list(map(int, input().rstrip().split()))
weights = list(map(int, input().rstrip().split()))
multiply = [vals[i]*weights[i] for i in range(n)]
print(round(sum(multiply)/sum(weights),1))
