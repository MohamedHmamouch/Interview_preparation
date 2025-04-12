

if __name__=='__main__':
    import math as m
    n,k=map(int,input().split())
    kk=k*m.ceil(n/k)
    print(m.ceil(kk/n))
    