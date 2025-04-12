


if __name__=='__main__':

    t=int(input())

    for _ in range(t):

        x,y=map(int,input().split())

        a,b=map(int,input().split())

        print(min(b*min(x,y)+a*abs(x-y),a*(x+y)))