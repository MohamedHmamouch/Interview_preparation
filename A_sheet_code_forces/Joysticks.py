

if __name__=='__main__':
    a,b=map(int,input().split())
    ans=0
    while max(a,b)>=2 and min(a,b)+1>=2:
        ans+=1
        if a>=b:
            a-=2
            b+=1
        else:
            b-=2
            a+=1
    print(ans)

    #    a1,a2=map(int,input().split())

    # charge=1
    # discharge=2
    # minutes=0

    # while a1 and a2:

    #     if a1<=a2:

    #         while a2>=1:

    #             a1+=charge
    #             a2-=discharge

    #             minutes+=1


    #     if a2<=a1:

    #         while a1>=1:

    #             a2+=charge
    #             a1-=discharge
    #             minutes+=1
    # print(minutes)