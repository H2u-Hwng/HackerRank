# Problem: https://www.hackerrank.com/challenges/30-sorting/problem
# Score: 30.0


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
count_swap = 0

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            count_swap += 1
            
print('Array is sorted in {} swaps.'.format(count_swap))
print('First Element: {}'.format(arr[0]))
print('Last Element: {}'.format(arr[n-1]))
