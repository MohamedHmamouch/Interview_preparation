
if __name__=='__main__'

n=int(input())

l=list(map(int,input().split()))

d={"evens":[], "odd":[]}

for i in range(len(l)):

    if l[i]%2==0:
        d["evens"].append(i+1)

    else:
        d["odd"].append(i+1)

if len(d["odd"])<len(d["evens"]):
    print(d["odd"][0])

else:
    print(d["evens"][0])