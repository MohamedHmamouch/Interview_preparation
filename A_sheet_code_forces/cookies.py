

if __name__=='__main__':

    number_cookies=int(input())

    l=list(map(int,input().split()))
    sum_coockies=sum(l)

    ways=0

    for i in range(len(l)):

        if (sum_coockies-l[i])%2==0:

            ways+=1

    print(ways)