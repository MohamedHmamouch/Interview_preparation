

if __name__=='__main__':

    n=int(input())
    l=[int(x) for x in str(n) ]
    count=0
    while len(l)!=1:

        new_sum=sum(l)
        l=[int(x) for x in str(new_sum)]
        count+=1

    print(count)

