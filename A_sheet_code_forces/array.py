

if __name__=='__main__':

    n=int(input())
    l=list(map(int,input().split()))
    l1=[] #negatif product
    l2=[] #positif product
    l3=[] #null product
    track_negatif=0
    index=-1
    
    for i in l:
    
        if i<0:
    
            l1.append(i)
    
            if len(l1)%2==0:
                l1.pop()
                l2.append(i)
                index=len(l2)-1
                track_negatif+=1
        elif i>0:
            l2.append(i)
    
        else:
            l3.append(i)
    
    print(len(l1),*l1)
    if track_negatif%2!=0 and index!=-1:
    
        l3.append(l2.pop(index))
    
    print(len(l2),*l2)
    print(len(l3),*l3)