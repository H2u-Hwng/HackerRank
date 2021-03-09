# Problem: https://www.hackerrank.com/challenges/py-set-add/problem
# Score: 10.0


n = int(input())
name_s = set()
for i in range(n):
    country = str(input())
    name_s.add(country)
print(len(name_s))
