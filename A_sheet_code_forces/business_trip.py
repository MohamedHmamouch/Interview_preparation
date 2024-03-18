

if __name__=='__main__':

    k=int(input())
    l=list(map(int,input().split()))

    l.sort(reverse=True)

    centimeter_gain=0
    num_month=0

    for i in l:

        if centimeter_gain<k:

            centimeter_gain+=i

            num_month+=1

    if centimeter_gain<k:

        print("-1")

    else:
        print(num_month)