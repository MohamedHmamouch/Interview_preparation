

if __name__=='__main__':

    n=int(input())
    s=str(input())

    res=""
    length=n

    for i in range(length):

        letter=s[i]

        if length%2!=0:

            mid=length//2
            res[mid]=s[i]

        else:

            mid=(length//2)-1
            res[mid]=s[i]
        
        length-=1

    print(res)