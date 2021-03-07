# Problem: https://www.hackerrank.com/challenges/nested-list/problem
# Score: 10.0


N = int(input())
nested_list = [[input(), float(input())] for _ in range(N)]
second_highest = sorted(list(set([marks for name, marks in nested_list])))[1]
print('\n'.join([a for a,b in sorted(nested_list) if b == second_highest]))
