# Problem: https://www.hackerrank.com/challenges/incorrect-regex/problem
# Score: 20.0


import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)
