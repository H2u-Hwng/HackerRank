# Problem: https://www.hackerrank.com/challenges/30-conditional-statements/problem
# Score: 30.0


n = int(input().strip())
if n % 2 != 0:
    print('Weird')
elif n % 2 == 0 and n in range(6,21):
    print('Weird')
else:
    print('Not Weird')
