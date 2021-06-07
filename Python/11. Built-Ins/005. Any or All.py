# Problem: https://www.hackerrank.com/challenges/any-or-all/problem
# Score: 20.0


n,nums = int(input()), list(map(int, input().strip().split()))

l = len(nums)

print(all([i>0 for i in nums]) and any([str(nums[j])==str(nums[j-l])[::-1] for j in range(l)]))
