

if __name__=='__main__':

    n=int(input())

    l=list(map(int,input().split()))

    check=[0 for _ in range(n)]


    for i in l:

        if i>n:
            continue

        check[i-1]=1

    print(check.count(0))