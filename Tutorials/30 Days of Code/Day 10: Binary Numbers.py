# Problem: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Score: 30.0


n = int(input().strip())

result = bin(n)[2:].split('0')

print(len(max(result)))
