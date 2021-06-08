# Problem: https://www.hackerrank.com/challenges/any-or-all/problem
# Score: 20.0


n = int(input()) 

nums = input().strip().split()

print(all([int(i)>0 for i in nums]) and any([j==j[::-1] for j in nums]))
