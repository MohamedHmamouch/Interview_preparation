


if __name__=='__main__':

    n=int(input())

    l=list(map(int,input().split()))

    s=set(l)

    if len(s)<=2:

        print("YES")

    elif len(s)>3:

        print("NO")

    else:

        m=max(s)
        mini=min(s)
        x=mini

        for i in s:

            if i not in [mini,m]:

                x=i

        if x-mini==m-x:

            print("YES")
            exit()
        else:
            print("NO")