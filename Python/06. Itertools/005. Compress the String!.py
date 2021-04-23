# Problem: https://www.hackerrank.com/challenges/compress-the-string/problem
# Score: 20.0


from itertools import groupby
s = input()
print(*[(len(list(c)), int(k)) for k, c in groupby(s)])
