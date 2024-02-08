if __name__=='__main__':

    n,a=map(int,input().split())
    l=list(map(int,input().split()))
    limak_pos=a-1
    move=0
    cant_catch=0
    total_criminal=l.count(1)

    while limak_pos-move>=0 and limak_pos+move<n:

        if l[limak_pos+move]+l[limak_pos-move]==1:

            cant_catch+=1

        move+=1

    print(total_criminal-cant_catch)

    # if n%2!=0:

    #     print(crimanls)

    # else:
    #     if l[-1]==1:

    #         print(crimanls)