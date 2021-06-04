# Problem: https://www.hackerrank.com/challenges/zipped/problem
# Score: 10.0


from statistics import mean

m,n = map(int, input().strip().split())
res = []

for _ in range(n):
    x = list(map(float, input().strip().split()))
    res.append(x)
    
for i in zip(*res):
    print(mean(i))
