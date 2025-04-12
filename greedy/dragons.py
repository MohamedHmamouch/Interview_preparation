


if __name__=='__main__':


    s,n=map(int,input().split())
    strength=[]
    for _ in range(n):

        x,y=map(int,input().split())

        strength.append([x,y])      

    strength.sort(key=lambda x:x[0])


    for st in strength:

        if s>st[0]:
            s+=st[1]


        elif s<=st[0]:

            print("NO")
            exit()

    print("YES")



