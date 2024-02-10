

if __name__=='__main__':

    n=int(input())
    l=list(map(int,input().split()))
    
    dollar=l[0]
    energy=0
    for i in range(n-1):
        
        if l[i]>=l[i+1]:
            
            energy+=l[i]-l[i+1]
            
        else:
            
            if energy >=l[i+1]-l[i]:
                
                energy-=l[i+1]-l[i]
                
            else:
                dollar+=l[i+1]-l[i]-energy
            
                energy=0
            
                
    print(dollar)