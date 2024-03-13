

if __name__=='__main__':

    n=int(input())

    num=list(map(int,input().split()))
    max_sequence=-float('inf')

    sequence=0
    l,r=0,1

    while r <len(num):

        if num[r]>=num[l]:
            sequence+=1
            r+=1
            l+=1


        else:
            max_sequence=max(max_sequence,sequence+1)
            sequence=0
            l=r
            r+=1
    max_sequence=max(max_sequence,sequence+1)
    print(max_sequence)


