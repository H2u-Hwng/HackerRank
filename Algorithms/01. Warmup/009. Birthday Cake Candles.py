# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Score: 10.0


candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
print(candles.count(max(candles)))
