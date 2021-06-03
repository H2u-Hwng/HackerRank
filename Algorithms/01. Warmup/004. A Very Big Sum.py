# Problem: https://www.hackerrank.com/challenges/a-very-big-sum/problem
# Score: 10.0


def aVeryBigSum(ar):
    print(sum(ar))

ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)
