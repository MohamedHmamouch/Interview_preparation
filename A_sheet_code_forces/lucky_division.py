

if __name__=='__main__':

    def is_lucky(x):
        
        # str_x=list(str(x))
        # lucky={4,7}
        # for i in str_x:
        #     if int(i) not in lucky:
        #         return False
        # return True

        while x:

            a=x%10
            if a!=4 and a!=7:
                return False
            
            x=x//10
            
        return True

    n=int(input())
    

    for i in range(1,n+1):

        if n%i==0:

            if is_lucky(i):

                print("YES")

                exit()

    print("NO")