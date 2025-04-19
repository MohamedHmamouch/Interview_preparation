n,target=map(int,input().split())
nums=list(map(int,input().split()))
d={0:1}

current=0
count=0
for n in nums:

    current+=n
    count+=d.get(current-target,0)
    d[current]=d.get(current,0)+1

print(count)

