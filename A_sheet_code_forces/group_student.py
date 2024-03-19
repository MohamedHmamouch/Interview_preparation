

if __name__=='__main__':

    n=int(input())

    l=list(map(int,input().split()))

    x,y=map(int,input().split())

    begineer=0
    intermediate=0
    for point in range(len(l)):

        rate=point+1
        begineer=0
        intermediate=0

        for point_prime in range(len(l)):

            if point_prime+1>=rate:
                intermediate+=l[point_prime]

            else:
                begineer+=l[point_prime]

        if intermediate<=y and intermediate>=x and begineer<=y and begineer>=x:


            print(rate)
            exit()

    print(0)