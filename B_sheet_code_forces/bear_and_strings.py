

if __name__=='__main__':
    # s=input()

    # i=0
    # last=0
    # length=len(s)
    # pairs=0



    s=input()

    i=0
    count=0
    n=len(s)
    l=0

    while i<n-3:
        
        substring=s[i]+s[i+1]+s[i+2]+s[i+3]
        
        if substring=="bear":
            
            indexes_after=len(range(l,i+1))
            
            indexes_before=len(range(i+3,n))
            
            count+=indexes_before*indexes_after
            
            i+=3
            l+=1
        else:
            i+=1            
    print(count)

    # while i<length-3:

    #     substring=s[i]+s[i+1]+s[i+2]+s[i+3]

    #     if substring=="bear":

    #         indexes_before=len(range(last,i+1))
    #         indexes_after=len(range(i+3,length))

    #         pairs+=indexes_after*indexes_before

    #         last=i+1
    #         i+=3

    #     else:
    #         i+=1

    # print(pairs)
