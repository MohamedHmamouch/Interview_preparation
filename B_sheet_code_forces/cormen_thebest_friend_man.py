




if __name__=='__main__':

    n,k=map(int,input().split())
    walks=list(map(int,input().split()))

    addition_walks=0

    for i in range(1,len(walks)):

        if k-walks[i-1]-walks[i]>0:
            addition_walks+=k-walks[i-1]-walks[i]
            walks[i]+=k-walks[i-1]-walks[i]

        else:
            continue

    print(addition_walks)
    print(*walks)
