

if __name__=='__main__':


    x=int(input())

    moves={1,2,3,4,5}

    if x in moves:

        print(1)

    else:

        if x%5==0:

            print(x//5)

        else:
            print((x//5) +1)