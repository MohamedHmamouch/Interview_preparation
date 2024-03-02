

if __name__=='__main__':


    n,k=map(int,input().split())


    l=list(map(int,input().split()))

    for i in range(1,len(l)):

        if l[i]>l[i-1]+1 and l[i]>l[i+1]+1:

            l[i]-=1
            k-=1

        if k==0:

            break


    for i in l:

        print(i,end=" ")