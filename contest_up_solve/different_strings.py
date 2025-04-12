

if __name__=='__main__':


    t=int(input())

    for _ in range(t):

        s=input()

        if len(set(s))==1:

            print("NO")

        else:

            sorted_string=sorted(s)

            print("YES")

            if ''.join(sorted_string)==s:

                sorted_string[0],sorted_string[-1]=sorted_string[-1],sorted_string[0]

            else:


                print(''.join(sorted_string))