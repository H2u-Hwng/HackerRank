# Problem: https://www.hackerrank.com/challenges/exceptions/problem
# Score: 10.0


for _ in range(int(input())):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except BaseException as e:
        print("Error Code:",e)
