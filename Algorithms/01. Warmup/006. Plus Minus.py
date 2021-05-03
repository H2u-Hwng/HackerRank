# Problem: https://www.hackerrank.com/challenges/plus-minus/problem
# Score: 10.0


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

print(format(len([x for x in arr if x > 0])/n,'.6f'))
print(format(len([x for x in arr if x < 0])/n,'.6f'))
print(format(len([x for x in arr if x == 0])/n,'.6f'))
