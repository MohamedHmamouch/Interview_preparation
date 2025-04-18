
n=int(input())
nums=list(map(int,input().split()))

maxsubbarray=nums[0]
current=0
for n in nums:

    if current<0:
        current=0

    current+=n
    maxsubbarray=max(maxsubbarray,current)

print(maxsubbarray)