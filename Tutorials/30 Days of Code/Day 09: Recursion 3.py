# Problem: https://www.hackerrank.com/challenges/30-recursion/problem
# Score: 30.0


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    print(result)

n = int(input().strip())
result = factorial(n)
