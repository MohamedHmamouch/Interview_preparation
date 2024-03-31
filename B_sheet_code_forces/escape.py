
if __name__=='__main__':

    vp=int(input())
    vd=int(input())
    t=int(input())
    f=int(input())
    c=int(input())

    if vd<=vp:
        print(0)
        exit()
        
    else:
        bijou=0
        
        dp=vp*t
        
        while dp<c:
            
            td=dp/(vd-vp) #catching princess
            
            
            
            if dp+td*vp>=c:
                
                break

            dp+=td*vp
            
            bijou+=1
            dp+=vp*(td+f)            
        print(bijou)
        
        
        
