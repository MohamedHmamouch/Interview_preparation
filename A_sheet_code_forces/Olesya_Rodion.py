

if __name__=='__main__':

    n,t=map(int,input().split())
    s=""

    if n<2 and t==10:

        print(-1)

        #there is no number with one digit and divisible by 10

    elif n>=2 and t==10:

        for _ in range(n-1):

            s+="5"

        s+="0"

    else:

        s=str(t)*n

    print(s)