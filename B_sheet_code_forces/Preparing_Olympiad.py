

if __name__=='__main__':

    n, l, r, x=map(int,input().split())

    c=list(map(int,input().split()))

    ways=0

    for i in range(1<<n):

        subset=[]

        sum_subset=0

        for j in range(n):

            if i & (1<<j):

                subset.append(c[j])
                sum_subset+=c[j]

        if len(subset)>=2:

            mini=min(subset)
            maxi=max(subset)

            if l<=sum_subset<=r and maxi-mini>=x:

                ways+=1

    print(ways)

