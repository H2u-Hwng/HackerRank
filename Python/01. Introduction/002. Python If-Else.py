# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Score: 10.0


n = int(input().strip())
if n in range (1,101):
  if (n%2 != 0) or (n%2 == 0 and n in range(6,21)):
    print('Weird')
  else:
    print('Not Weird')
