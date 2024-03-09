
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


    # mat=[]

    # for _ in range(n):

    #     mat.append(list(input()))

    # first_diag=mat[0][0]
    # second_diag=mat[0][n-1]
    # ref=mat[0][1]
    # unique=set()
    # for i in range(len(mat)):

    #     for j in range(len(mat)):

    #         if mat[i][i]!=first_diag or mat[i][n-1-i]!=second_diag:

    #             print("NO")
    #             exit()

    #         elif i!=j and j!=n-1-i:
    #               if mat[i][j]!=ref or mat[i][j]==first_diag or mat[i][j]==second_diag:

    #                 print("NO")
    #                 exit()
    # print("YES")





