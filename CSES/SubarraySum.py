n,target=map(int,input().split())
nums=list(map(int,input().split()))

count=0
total=0
l=0

for r in range(n):

    total+=nums[r]

    while l<r and total>target:

        total-=nums[l]
        l+=1

    if total==target:
        count+=1

print(count)