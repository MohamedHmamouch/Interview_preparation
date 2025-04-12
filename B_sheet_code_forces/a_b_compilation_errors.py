

if __name__=='__main__':

    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    c=list(map(int,input().split()))
    first_error=abs(sum(a)-sum(b))

    second_error=abs(sum(b)-sum(c))

    print(first_error)
    print(second_error)

    








