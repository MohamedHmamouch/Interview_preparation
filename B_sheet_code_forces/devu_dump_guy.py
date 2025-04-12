


if __name__=='__main__':



    n,x=map(int,input().split())

    c=list(map(int,input().split()))

    c.sort()

    hours=0
    i=0
    while x!=0 and i<n:

        hours+=c[i]*x
        i+=1
        x-=1

    hours+=sum(c[i:])

    print(hours)


