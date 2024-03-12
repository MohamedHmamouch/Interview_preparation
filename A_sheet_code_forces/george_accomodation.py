

if __name__=='__main__':
    n=int(input())
    available=0

    for _ in range(n):


        p,q=map(int,input().split())

        left_places=q-p

        if left_places>=2:
            available+=1

    print(available)