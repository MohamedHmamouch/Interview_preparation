


if __name__=='__main__':

    n=int(input())
    res=0

    for i in range(1,n+1):        # print(res)

        res+=((-1)**i)*i
    
    print(res)
