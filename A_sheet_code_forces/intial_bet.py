

if __name__=='__main__':

    l=list(map(int,input().split()))

    total_sum=sum(l)
    if total_sum==0:
        print(0)
    elif total_sum%5!=0 or total_sum==0:
        print("-1")

    else:
        print(total_sum//5)