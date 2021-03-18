# Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem
# Score: 10.0


from itertools import combinations 
s, k = input().split()
for i in range(1,int(k)+1):
    comb = list(combinations(sorted(s), i))
    [print(''.join(j)) for j in comb]
