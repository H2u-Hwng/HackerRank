# Problem: https://www.hackerrank.com/challenges/arrays-ds/problem
# Score: 10.0


def reverseArray(a):
    print(*a[::-1])    
    
arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
res = reverseArray(arr)
