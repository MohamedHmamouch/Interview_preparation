


if __name__=='__main__':

    n,m=map(int,input().split())

    cont=[]

    for _ in range(m):

        a,b=map(int,input().split())

        cont.append([a,b])

    cont.sort(key=lambda x:x[1], reverse=True)


    take=0

    for a,b in cont:

        take+=min(a,n)*b
        n-=min(a,n)

    print(take)