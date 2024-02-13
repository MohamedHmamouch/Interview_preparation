

if __name__=='__main__':

    n,m,c=input().split()

    dep=[c]
    n=int(n)
    m=int(m)
    mat=[]

    for _ in range(n):
        
        mat.append(list(input()))
        
        

    for i in range(n):
        
        for j in range(m):
            
            if mat[i][j]==c:
            
                if i!=0:
                    
                    if mat[i-1][j]!="." and mat[i-1][j] not in dep:
                        
                        dep.append(mat[i-1][j])
                        
                if i!=n-1:
                    
                    if mat[i+1][j]!="." and mat[i+1][j] not in dep:
                        
                        dep.append(mat[i+1][j])
                        
                if j!=0:
                    
                    if mat[i][j-1]!="." and mat[i][j-1] not in dep:
                        
                        dep.append(mat[i][j-1])
                        
                if j!=m-1:
                    
                    if mat[i][j+1]!="." and mat[i][j+1] not in dep:
                        
                        dep.append(mat[i][j+1])
                        
    print(len(dep)-1)
                
                
            
            
            

