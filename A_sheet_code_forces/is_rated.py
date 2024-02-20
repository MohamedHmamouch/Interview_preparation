

if __name__=='__main__':

    n=int(input())
    is_rated=False
    after=[]
    before=[]
    for _ in range(n):

        a,b=map(int,input().split())

        if a-b!=0:

            is_rated=True

        after.append(a)
        before.append(b)

    sorted_a=sorted(after,reverse=True)


    if is_rated:

            print("rated")
    else:

        if after!=sorted(after,reverse=True):
            print("unrated")

        else:

            print("maybe")

