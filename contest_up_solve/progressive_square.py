

if __name__=='__main__':

    t=int(input())
    

    for _ in range(t):

        n,c,d=map(int,input().split())

        l=list(map(int,input().split()))

        a1=sorted(l)[0]

        res=[]

        for i in range(n):

            for j in range(n):

                res.append(a1+i*c +j*d)

        
        if sorted(res)==sorted(l):

            print("YES")

        else:

            print("NO")
            