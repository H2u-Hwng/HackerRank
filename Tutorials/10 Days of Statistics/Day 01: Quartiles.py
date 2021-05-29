# Problem: https://www.hackerrank.com/challenges/s10-quartiles/problem
# Score: 30.0


from statistics import median  
     
n = int(input().strip())
data = list(map(int, input().rstrip().split()))
data.sort()

m = n//2
l = data[:m]
if n%2 == 0:
    u = data[m:]
else:  
    u = data[m+1:]
     
print(int(median(l)))
print(int(median(data)))
print(int(median(u)))
