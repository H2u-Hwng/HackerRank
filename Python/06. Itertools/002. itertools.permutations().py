# Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Score: 10.0


from itertools import permutations
s, k = input().split()
per = list(permutations(s, int(k)))
per.sort()
[print(''.join(i)) for i in per]
