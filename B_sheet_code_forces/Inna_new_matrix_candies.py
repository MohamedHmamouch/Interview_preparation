

if __name__=='__main__':

    n,m=map(int,input().split())
    mat=[]

    min_distance=float('inf')
    s=set()

    for _ in range(n):

        cells=list(input())

        
        candy_index=cells.index("S")
        dawrf_index=cells.index("G")
        distance=candy_index-dawrf_index

        if distance<0:

            print("-1")
            break

        else:

            s.add(distance)

    print(len(s))