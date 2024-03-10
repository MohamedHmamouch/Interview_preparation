

if __name__=='__main__':


    n,k=map(int,input().split())

    l=list(map(int,input().split()))

    refrence=l[k-1]
    passed=0

    for i in range(len(l)):

        if l[i]>=refrence and l[i]>0:

            passed+=1
    print(passed)