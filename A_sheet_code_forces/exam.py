

if __name__=='__main__':


    n=int(input())
    even,odd=[],[]

    if(n==1):
        print(1)
        print(1)
    elif(n==2):
        print(1)
        print('1')
    elif(n==3):
        print(2)
        print('1 3')
    elif(n==4):
        print(4)
        print('3 1 4 2')

    else:


        for i in range(1,n+1):

            if i%2==0:
                even.append(i)

            else:
                odd.append(i)
        
        even=sorted(even,reverse=True)
        odd=sorted(odd,reverse=True)
        num=even+odd
        print(len(num))
        print(*num)



    

        


