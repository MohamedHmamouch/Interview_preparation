

if __name__=='__main__':

    n=int(input())

    first=0
    second=0
    count_first=0
    count_second=0
    X=[]
    Y=[]

    for i in range(n):

        a=int(input())

        if a>0:

            first+=a
            count_first+=1
            X.append(a)

        else:

            second+=(-1)*a
            count_second+=1
            Y.append(a)

    
    if first>second:

        print("first")

    elif second>first:
        print("second")

    elif first==second:

        if len(X)>len(Y) and all(X)==all(Y):

            print("first")

        else:

            print("second")


    