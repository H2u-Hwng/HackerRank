# Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Score: 10.0


a = int(input())
set_a = set(input().split())
n = int(input())
for _ in range(n):
    cmd, _ = input().split()
    set_b = set(input().split())
    getattr(set_a, cmd)(set_b)   
print(sum(map(int, set_a)))
