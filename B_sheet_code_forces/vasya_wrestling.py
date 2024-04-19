

if __name__=='__main__':

    n=int(input())

    first=0
    second=0
    count_first=0
    count_second=0
    X=[]
    Y=[]
    last=0

    for i in range(n):

        a=int(input())

        if a>0:

            first+=a
            X.append(a)
            last=1

        else:

            second+=(-1)*a
            Y.append(-a)
            last=0

    if first>second:

        print("first")

    elif second>first:
        print("second")

    elif first==second:

        print("first" if last else "second")
            
        else:
            print("first" if X>Y else "second")

    