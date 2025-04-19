n, k = map(int, input().split())
nums = list(map(int, input().split()))

d = {}
l = 0
count = 0

for r in range(n):
    d[nums[r]] = d.get(nums[r], 0) + 1

    while len(d) > k:
        d[nums[l]] -= 1
        if d[nums[l]] == 0:
            del d[nums[l]]
        l += 1

    count += (r - l + 1)

print(count)
