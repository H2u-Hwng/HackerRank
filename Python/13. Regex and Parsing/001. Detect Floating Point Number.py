# Problem: https://www.hackerrank.com/challenges/introduction-to-regex/problem
# Score: 20.0


for _ in range(int(input())):
    try:
        if float(input()) or  float(input())==0.0:
            print(True)
    except Exception:
        print(False)
