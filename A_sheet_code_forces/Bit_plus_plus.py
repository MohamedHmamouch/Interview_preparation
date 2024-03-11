

if __name__=='__main__':


    n=int(input())

    intial=0

    for _ in range(n):

        s=input()

        if s.__contains__('+'):
            intial+=1

        else:

            intial-=1

    print(intial)