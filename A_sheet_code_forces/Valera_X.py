
if __name__=='__main__':


    n=int(input())

    diag=[]
    arr=[]

    for _ in range(n):

        arr.append(input())

    c1=arr[0][0]
    c2=arr[0][1]
    ans=c1!=c2

    for i in range(n):

        for j in range(n):

            if i==j and c1!=arr[i][j]:

                ans=False

            if i==n-1-j and c1!=arr[i][j]:

                ans=False

            if i!=j and i!=n-1-j and c2!=arr[i][j]:

                ans=False

    if ans:

        print("YES")

    else:
        print("NO")





