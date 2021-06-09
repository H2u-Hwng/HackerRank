# Problem: https://www.hackerrank.com/challenges/big-sorting/problem
# Score: 20.0


def bigSorting(unsorted):
    unsorted.sort(key=int)
    for s in unsorted:
        print(s)

n = int(input().strip())

unsorted = []

for _ in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)

result = bigSorting(unsorted)
