# Problem: https://www.hackerrank.com/challenges/string-validators/problem
# Score: 10.0


txt = input()
for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(method(i) for i in txt))
