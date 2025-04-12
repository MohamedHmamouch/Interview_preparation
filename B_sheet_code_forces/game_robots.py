

if __name__=='__main__':

    
    n,k=map(int,input().split())

    l=list(map(int,input().split()))

    L=[]

    for i in range(n):
        
        for j in range(0,i):

            L.append(l[j])

            if len(L)>=k:
                # print(L)
                print(L[k-1])

                exit()

        

    # print(L)


