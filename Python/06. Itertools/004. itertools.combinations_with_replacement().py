# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Score: 10.0


from itertools import combinations_with_replacement
s, k = input().split()
comb_wr = list(combinations_with_replacement(sorted(s), int(k)))
[print(''.join(i)) for i in comb_wr]
