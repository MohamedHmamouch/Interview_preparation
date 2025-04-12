


if __name__=='__main__':


    t=int(input())

    for _ in range(t):

        n=int(input())

        l=list(map(int,input().split()))


        left=1

        while left<n and l[left]==l[left-1]:

            left+=1

        if left==n:
            print(0)
            continue

        right=n-2

        while right>=0 and l[right]==l[right+1]:

            right-=1


        if l[0]==l[-1]:

            print(right-left+1)

        else:

            print(min(n-left,right+1))
