# Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Score: 10.0


n = int(input())
s = set(map(int, input().split()))
num = int(input())
for op in range(num):
    op = input().split()
    if op[0] == "pop" :
        s.pop()
    elif op[0] == "remove" :
        s.remove(int(op[1]))
    elif op[0] == "discard" :
        s.discard(int(op[1]))
print(sum(s))
