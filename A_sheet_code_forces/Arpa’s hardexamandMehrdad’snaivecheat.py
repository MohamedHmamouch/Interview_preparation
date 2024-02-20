

if __name__=='__main__':

    n=int(input())

    last_digit=[8,4,2,6]
    print(1378**n)

    if n==0:

        print(1)
    else:

        n=(n-1)%4

        print(last_digit[n])