

if __name__=="__main__":

    n,f=map(int,input().split())
    profit=0
    days=[0]*n
    for i in range(n):

        k,l=map(int,input().split())

        profit+=min(k,l)

        if l>k:

            days[i]=min(2*k,l)-min(k,l)

        else:

            days[i]=0

    days.sort(reverse=True)
    days=days[:f]

    profit+=sum(days)

    print(profit)