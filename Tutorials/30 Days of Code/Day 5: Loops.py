# Problem: https://www.hackerrank.com/challenges/30-loops/problem
# Score: 30.0


n = int(input().strip())
for i in range(1,11):
    print('{} x {} = {}'.format(n,i,n*i))
