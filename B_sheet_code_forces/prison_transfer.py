

if __name__=='__main__':

    n,t,c=map(int,input().split())
    p=list(map(int,input().split()))
    
    ans,count=0,0

    for i in p:

        if i<=t:

            count+=1

        else:
            count=0

        if count>=c:

            ans+=1

    print(ans)



