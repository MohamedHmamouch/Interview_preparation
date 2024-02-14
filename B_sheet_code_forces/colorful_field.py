



if __name__=='__main__':

    n,m,k,t=map(int,input().split())

    matrix=[]

    for _ in range(k+t):
        a,b=map(int,input().split())
        matrix.append([a,b])

    matrix.sort(key=lambda x:x[0])

    print(matrix)

