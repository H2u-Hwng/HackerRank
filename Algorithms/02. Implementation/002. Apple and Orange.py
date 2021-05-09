# Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Score: 10.0


first_multiple_input = input().rstrip().split()
s = int(first_multiple_input[0])
t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()
a = int(second_multiple_input[0])
b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()
m = int(third_multiple_input[0])
n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

print(sum([1 for x in apples if (x + a) in range(s,t+1)]))
print(sum([1 for x in oranges if (x + b) in range(s,t+1)]))
