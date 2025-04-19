n=int(input())
nums=list(map(int,input().split()))

from collections import defaultdict
d=defaultdict(int)
d[0]=1
count=0
prefix_sum=0
for i in nums:
    prefix_sum+=i
    remainder=prefix_sum%n
    count+=d[remainder]
    d[remainder]+=1

print(count)