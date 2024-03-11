

if __name__=='__main__':

    # n=int(input())

    # s=list(input())

    # l,r=0,1

    # while r<len(s):

    #     if (s[l]=='1' and s[r]=='0') or (s[l]=='0' and s[r]=='1'):

    #         s.remove(s[l])
    #         s.remove(s[r-1])
    #         l=0
    #         r=1

    #     else:

    #         l+=1
    #         r+=1
    # print(len(s))

    n=int(input())



    s=list(input())

    count_ones=s.count('1')
    count_zeros=s.count("0")

    print(abs(count_zeros-count_ones))