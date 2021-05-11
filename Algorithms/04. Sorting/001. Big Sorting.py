# Problem: https://www.hackerrank.com/challenges/big-sorting/problem
# Score: 20.0


n = int(input().strip())
unsorted = []
for _ in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)
for elem in sorted(unsorted, key=int):
    print(elem)
