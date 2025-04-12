
if __name__=='__main__':


    n,k=map(int,input().split())

    result=[]
    for i in range(n):

        res=""
        if i%2==0:

            for j in range(n):

                if j%2==0 and k>0:

                    res+="L"
                    k-=1

                else:

                    res+="S"
        else:
            for j in range(n):

                if j%2!=0 and k>0:

                    res+="L"
                    k-=1

                else:

                    res+="S"

        result.append(res)

    if k>0:

        print("NO")

    else:


        for i in result:

            print(i)
