



if __name__=='__main__':


    n,k=map(int,input().split())
    coverd_num=0

    for _ in range(n):


        a,b=map(int,input().split())

        coverd_num+=abs(a-b)+1
    
    if coverd_num%k==0:

        print(0)
    else:

        remainder=coverd_num%k

        print(k-remainder)

