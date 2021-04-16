# Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem
# Score: 10.0


import math
ab = int(input())
bc = int(input())
print(str(round(math.degrees(math.atan2(ab,bc)))) + u"\N{DEGREE SIGN}")
