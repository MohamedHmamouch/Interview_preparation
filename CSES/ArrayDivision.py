n, k = map(int, input().split())
nums = list(map(int, input().split()))

def CanSplit(largest):
    subarray = 1
    total = 0
    for n in nums:
        if total + n > largest:
            subarray += 1
            total = n
        else:
            total += n
    return subarray <= k

l, r = max(nums), sum(nums)

while l < r:
    mid = (l + r) // 2
    if CanSplit(mid):
        r = mid
    else:
        l = mid + 1

print(l)
