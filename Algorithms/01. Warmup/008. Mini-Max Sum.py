# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Score: 10.0


def miniMaxSum(arr):
    arr.sort()
    minium = sum(arr[:-1])
    maxium = sum(arr[1:])
    print(minium, maxium)

arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)
