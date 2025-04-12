

if __name__=='__main__':

    n=int(input())
    l=list(map(int,input().split()))

    min_val=l[0]
    index_min_val=0
    d={}

    for i in range(len(l)):
        d[l[i]]=d.get(l[i],0)+1

        if l[i]<min_val:

            min_val=l[i]
            index_min_val=i


    if d[min_val]>1:
        print("Still Rozdil")

    else:
        print(index_min_val+1)



