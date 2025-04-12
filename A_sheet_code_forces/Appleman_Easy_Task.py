

if __name__=='__main__':

    n=int(input())
    mat=[]
    for _ in range(n):

        mat.append(list(input()))
    couples=[]
    if n==1:

        print("YES")

    else:

        for i in range(n):

            for j in range(n):

                connection=0

                if i==0 and j!=n-1 and j!=0:

                    if mat[i][j+1]=="o":
                        connection+=1

                    if mat[i+1][j]=="o":
                        connection+=1

                    if mat[i][j-1]=="o":
                        connection+=1

                if i==0 and j==n-1:

                    if mat[i][j-1]=="o":
                        connection+=1

                    if mat[i+1][j]=="o":
                        connection+=1
    

                if i!=0 and i!=n-1 and j!=n-1 and j>0:

                    if mat[i-1][j]=="o":
                        connection+=1

                    if mat[i][j+1]=="o":
                        connection+=1

                    if mat[i+1][j]=="o":
                        connection+=1

                    if mat[i][j-1]=="o":
                        connection+=1

                if i==n-1 and j!=n-1:
                    if mat[i][j-1]=="o":
                        connection+=1

                    if mat[i-1][j]=="o":
                        connection+=1

                    if mat[i][j+1]=="o":
                        connection+=1


                if i==n-1 and j==n-1:

                    if mat[i][j-1]=="o":
                        connection+=1

                    if mat[i-1][j]=="o":
                        connection+=1

                if connection%2!=0:
                    print(i,j)
                    print(connection)
                    print("NO")

                    exit()

        print("YES")
        