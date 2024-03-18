

if __name__=='__main__':

    n,x=map(int,input().split())

    x_divisors=set()
    for i in range(1,n+1):

        if x%i==0 and x//i<=n:
            x_divisors.add(i)

    # if x>n:
    #     x_divisors.remove(1)
    #     print(len(x_divisors))

    # else:
    print(len(x_divisors))
