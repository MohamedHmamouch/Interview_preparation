

if __name__=='__main__':

    l=list(map(int,input().split()))
    l.sort()
    mid=len(l)//2

    min_distance=(l[mid]-l[0])+(l[2]-l[mid])
    print(min_distance)

    