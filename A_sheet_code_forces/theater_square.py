

if __name__=='__main__':

    n,m,a=map(int,input().split())

    width=n//a

    if n%a>0:
        
        width+=1
        
    height=m//a

    if m%a>0:
        
        height+=1
        
    print(height*width)