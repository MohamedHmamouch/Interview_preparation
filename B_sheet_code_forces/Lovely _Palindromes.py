
if __name__=='__main__':


    n=int(input())

    # correct answer but do not satisfy time complexiy

    # if n>=1 and n<10:

    #     print(n*11)

    # else:

    #     s=str(n)
    #     s+=s[::-1]

    #     print(int(s))

    if n>=1 and n<10:

        print(n*11)

    else:

        s=str(n)
        new_s=list(s)
        
        l,r=0,len(s)-1

        while l<r:

            new_s[l],new_s[r]=new_s[r],new_s[l]

            l+=1
            r-=1

        s+=''.join(new_s)

        print(s)

        

