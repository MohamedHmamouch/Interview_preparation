

if __name__=='__main__':
    import math

    n,a,b=map(int,input().split())

    x=list(map(int,input().split()))

    for i in x:

        # print(math.floor(i*a/b),end=" ")
        print(((i*a)%b)//a,end=" ")
        