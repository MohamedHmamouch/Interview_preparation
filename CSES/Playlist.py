n = int(input())
nums = list(map(int, input().split()))

l = 0
maxSubarray = 0
d = {}

for r in range(n):
    d[nums[r]] = d.get(nums[r], 0) + 1
    while d[nums[r]] > 1:
        d[nums[l]] -= 1
        if d[nums[l]] == 0:
            del d[nums[l]]
        l += 1
    maxSubarray = max(maxSubarray, len(d))

print(maxSubarray)
