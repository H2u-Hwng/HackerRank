# Problem: https://www.hackerrank.com/challenges/array-left-rotation/problem
# Score: 20.0


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))
shifted = arr[d%n:] + arr[:d%n]
for num in shifted:
    print(num, end=' ')
