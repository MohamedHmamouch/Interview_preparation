
import math
if __name__=='__main__':


    n=int(input())
    b=[]
    val=0

    for i in range(n):

        a=int(input())

        if a%2==0:

            b.append(a//2)

        else:

            if val==0:

                b.append(math.ceil(a/2))

                val=1

            else:

                b.append(math.floor(a/2))

                val=0

    for i in b:

        print(i)
