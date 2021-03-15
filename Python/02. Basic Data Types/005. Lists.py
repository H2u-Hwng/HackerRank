# Problem: https://www.hackerrank.com/challenges/python-lists/problem
# Score: 10.0


n = int(input())
arr = list()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'print':
        print(arr)
    elif len(cmd) == 1:
        getattr(arr, cmd[0])()
    elif len(cmd) == 2:
        getattr(arr, cmd[0])(int(cmd[1]))
    elif len(cmd) == 3:
        getattr(arr, cmd[0])(int(cmd[1]), int(cmd[2]))
