

if __name__=='__main__':


    n=int(input())
    l=list(map(int,input().split()))

    if len(l)==1:

        print("YES")

    else:

        d={}

        for i in l:

            if i in d:

                d[i]+=1

            else:
                d[i]=1

        max_duplicated_val=max(v for _,v in d.items())


        if len(l)%2==0:

            if max_duplicated_val<=len(l)//2:

                print("YES")
            else:

                print("NO")

        elif len(l)%2!=0:

            if max_duplicated_val<=len(l)//2 +1:

                print('YES')

            else:

                print("NO")        
        
    