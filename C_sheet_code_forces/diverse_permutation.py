


if __name__=='__main__':


    n,k=map(int,input().split())



    l=[]
    x=n
    y=1
    for i in range(k):

        if i%2==0:

            l.append(x)

            x-=1

        else:
            l.append(y)
            y+=1

    
    low=0
    t=0

    if k%2==0:

        low=y
        t=1

    else:

        low=x
        t=-1

    for i in range(n-k):

        l.append(low)
        low+=t