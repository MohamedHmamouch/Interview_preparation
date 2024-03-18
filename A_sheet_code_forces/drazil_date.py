

if __name__=='__main__':
    import math

    a,b,s=map(int,input().split())

    if s>=abs(a)+abs(b) and (s-(abs(a)+abs(b)))%2==0:
        print("Yes")

    else:
      print("No")
