length=int(input())
nums=list(map(int,input().split()))

moves=0
increase=0

l=0
r=1
while r<length:

    if nums[l]<=nums[r]:
        l+=1
        r+=1

    else:

        moves+=abs(nums[r]-nums[l])
        nums[r]+=abs(nums[r]-nums[l])
        l+=1
        r+=1

print(moves)

        