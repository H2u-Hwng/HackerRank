# Problem: https://www.hackerrank.com/challenges/2d-array/problem
# Score: 15.0


def hourglassSum(arr,x,y):
    top = arr[x][y] + arr[x][y+1] + arr[x][y+2]
    mid = arr[x+1][y+1]
    bottom = arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
    return top+mid+bottom

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

res = -999999
for x in range(6-2):
    for y in range(6-2):
        temp = hourglassSum(arr,x,y)
        if temp > res:
            res = temp

print(res)
