

if __name__=='__main__':

    n=int(input())

    l=[]


    for _ in range(n):
        price,quality=map(int,input().split())
        l.append([price,quality])

    l.sort(key=lambda x:(x[0]))
    
    for i in range(1,len(l)):

        if l[i][1]<l[i-1][1]:

            print("Happy Alex")

            exit()

    
    print("Poor Alex")

        

    

