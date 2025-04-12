

if __name__=='__main__':

    n=int(input())

    string=input()

    s=set()
    change=0
    for i in range(n):

        for j in range(i+1,n+1):

            substring=string[i:j]
            print(substring)

            if substring in s:

                change+=1

            else:

                s.add(substring)

    print(change)

