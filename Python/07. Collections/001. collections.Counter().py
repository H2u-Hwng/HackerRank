# Problem: https://www.hackerrank.com/challenges/collections-counter/problem
# Score: 10.0


from collections import Counter
x = int(input())
shoes = Counter(map(int, input().split()))
n = int(input())
income = 0
for _ in range(n):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1
print(income)
