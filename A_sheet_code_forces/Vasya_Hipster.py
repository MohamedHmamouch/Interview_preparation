


if __name__=='__main__':


    n,m=map(int,input().split())

    maximum_fashionable=min(n,m)

    left=abs(n-m)
    num_of_day_same_socks=left//2

    print(maximum_fashionable,num_of_day_same_socks)






