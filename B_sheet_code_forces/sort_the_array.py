

if __name__=='__main__':

    n=int(input())
    l=list(map(int,input().split()))

    i=1

    while l[i-1]<l[i]:

        i+=1

    j=i

    while j <n and l[j-1]>l[j]:

        j+=1

    # print(l[:i-1])
    # print(l[i-1:j][::-1])
    # print(l[j:])

    if l[:i-1]+l[i-1:j][::-1]+l[j:]==sorted(l):

        print("yes")
        print(i,j)

    else:

        print("no")
