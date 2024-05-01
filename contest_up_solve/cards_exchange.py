


if __name__=='__main__':

    t=int(input())

    for _ in range(t):

        n,k=map(int,input().split())

        c={}

        nums=list(map(int,input().split()))

        for i in nums:

            if i in c:
                c[i]+=1

            else:
                c[i]=1

        ans=n
        
        for index,v in c.items():

            if v>=k:

                ans=k-1

        print(ans)