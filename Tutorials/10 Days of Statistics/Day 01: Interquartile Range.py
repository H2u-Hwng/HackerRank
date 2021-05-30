# Problem: https://www.hackerrank.com/challenges/s10-interquartile-range/problem
# Score: 30.0


import itertools
from statistics import median

n = int(input().strip())
val = list(map(int, input().rstrip().split()))
freq = list(map(int, input().rstrip().split()))
res = []
for i in range(n):
    res2 = list(itertools.repeat(val[i],freq[i]))
    for j in res2:
        res.append(j)
res.sort()
m = len(res)//2
l = res[:m]
if n%2 == 0:
    u = res[m:]
else:  
    u = res[m+1:]
print(round(float(median(u))-float(median(l)),1))
