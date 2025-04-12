

if __name__=='__main__':

    n,m=map(int,input().split(' ',1))
    listt=[]
    for x in range(n):
        list1=list(map(int,input().split(' ',m-1)))
        listt.append(list1)
    steps=4
    for i in range(n):
        for j in range(m):
            if listt[i][j]==1 and (j==0 or j==m-1 or i==0 or i==n-1):
                steps=2
                break
    print(steps)
        


        