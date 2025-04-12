

if __name__=='__main__':
    n,k,l,r,sall,sk=map(int,input().split())
    if sall != sk:
        ak=[sk//k]*k
        a=[(sall-sk)//(n-k)]*(n-k)
        for i in range(sk%k):
            print(ak[i]+1,end=' ')
        for i in range(sk%k,k):
            print(ak[i],end=' ')
        for i in range((sall-sk)%(n-k)):
            print(a[i]+1,end=' ')
        for i in range((sall-sk)%(n-k),n-k):
            print(a[i],end=' ')
    else:
        ak=[sk//k]*k
        for i in range(sk%k):
            print(ak[i]+1,end=' ')
        for i in range(sk%k,k):
            print(ak[i],end=' ')