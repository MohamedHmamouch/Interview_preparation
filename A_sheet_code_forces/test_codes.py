


if __name__=='__main__':


    # n,k=map(int,input().split())
    # not_good=0

    # k_digits=[i for i in range(k+1)]
    # for _ in range(n):
        
    #     num=input()
    #     list_num=list(num)
        
    #     for i in k_digits:
            
    #         if str(i) not in list_num:
                
    #             not_good+=1
                
    #             break
            
            
    # print(n-not_good)

    # n,m=map(int,input().split())
    # counter=0
    # remainder=[0]*5

    # for i in range(1,min(n,m)+1):

    
    #     rem=i%5
    #     remainder[rem]+=1


    # for j in range(1,max(n,m)+1):

    #     rem=j%5

    #     counter+=remainder[(5-rem)%5]


    # print(counter)


    # n,k=map(int,input().split())
 
    # l=list(map(int,input().split()))
    
    # for i in range(1,len(l)-1):
        
    #     if l[i] >l[i-1]+1 and l[i]>l[i+1]+1 and k>0:
            
    #         l[i]-=1
    #         k-=1
    
    # for j in l:
        
    #     print(j,end=" ")

    # l1,l2=map(str,input().split('|'))

    # s=input()

    # for i in range(len(s)):

    #     if len(l1)>len(l2):

    #         l2+=s[i]

    #     else:

    #         l1+=s[i]

    # if len(l1)==len(l2):

    #     print(f"{l1}|{l2}")

    # else:

    #     print("Impossible")

    # n=int(input())

    # moves=list(input())

    # coordinates=list(map(int,input().split()))
    # min_colision_time=float('inf')


    # for i in range(len(moves)-1):

    #     if moves[i]=='R' and moves[i+1]=='L':
            
    #         time_collision=(coordinates[i+1]-coordinates[i])//2

    #         min_colision_time=min(time_collision,min_colision_time)

    # if min_colision_time!=float('inf'):

    #     print(min_colision_time)
    # else:
    #     print(-1)

    # n,k=map(int,input().split())
    # covers=0
    # for _ in range(n):

    #     l,r=map(int,input().split())

    #     covers+=r-l+1

    # if covers%k==0:
    #     print(0)
    # else:

    #     print(k-covers%k)

    # mat=[]

    # for _ in range(4):

    #     li=list(input())
    #     mat.append(li)

    # for i in range(3):

    #     for j in range(3):
    #         count_black=0
    #         count_white=0

    #         for k in range(2):
    #             for l in range(2):

    #                 if mat[i+k][j+l]=="#":

    #                     count_black+=1
    #         count_white=4-count_black

    #         if count_black>=3 or count_white>=3:

    #             print("YES")

    #             exit()

    # print("NO")

    # n=int(input())

    # l=list(map(int,input().split()))

    # d={}
    # max_repition=0

    # for i in l:

    #     d[i]=1+d.get(i,0)

    #     max_repition=max(max_repition,d[i])

    # if n%2==0:

    #     if max_repition<=n//2:

    #         print('YES')

    #     else:
    #         print("NO")
    # elif n%2!=0:

    #     if max_repition<=(n//2)+1:

    #         print('YES')

    #     else:
    #         print('NO')

    # n,m=map(int,input().split())
 
    
    
    # for i in range(n+1,m+1):
        
    #     divisors=[]
    #     for k in range(1,i+1):
            
    #         if i%k==0:
                
    #             divisors.append(k)
                
    #     if len(divisors)==2 and divisors[0]==1 and divisors[1]==i:

    #         next_prime=k
            
            
    
    # print("NO")
    # n=int(input())
    # # if n==0:
    # #     print(1)
    # # else:
    # sequence=[1,8,4,2,6]
    # print(sequence[(n-1)%4])

    # n=int(input())

    # mat=[]

    # for _ in range(n):

    #     mat.append(list(input()))

    # first_diag=mat[0][0]
    # second_diag=mat[0][n-1]
    # ref=mat[0][1]
    # unique=set()
    # for i in range(len(mat)):

    #     for j in range(len(mat)):

    #         if mat[i][i]!=first_diag or mat[i][n-1-i]!=second_diag:

    #             print("NO")
    #             exit()

    #         elif i!=j and j!=n-1-i:
    #               if mat[i][j]!=ref or mat[i][j]==first_diag or mat[i][j]==second_diag:

    #                 print("NO")
    #                 exit()
    # print("YES")

    # n,m=map(int,input().split())

    # color={'C','M','Y'}
    # photo_colors=[]

    # for _ in range(n):

    #     l=list(map(str,input().split()))
        
    #     for i in l:

    #         if i in color:
    #             print("#color")
    #             exit()
                

    # print("#Black&White")


    # n,t=map(int,input().split())

    # if n==1 and t==10:

    #     print(-1)

    # elif n>=1 and t!=10:

    #     s=[t]*n
    #     s=int("".join(map(str,s)))
    #     print(s)


    # elif n>1 and t==10:
    #     s=int("5"+"0"*(n-1))
    #     print(s)

    # assert s%t==0


    # n=int(input())

    # l=list(map(int,input().split()))

    # d={"evens":[], "odd":[]}

    # for i in range(len(l)):

    #     if l[i]%2==0:
    #         d["evens"].append(i+1)

    #     else:
    #         d["odd"].append(i+1)

    # if len(d["odd"])<len(d["evens"]):
    #     print(d["odd"][0])

    # else:
    #     print(d["evens"][0])

    # levels=int(input())

    # passes=[False]*(levels+1)

    # X=list(map(int,input().split()))[1:]
    # Y=list(map(int,input().split()))[1:]

    # for i in range(len(X)):

    #     passes[X[i]]=True

    # for j in range(len(Y)):

    #     passes[Y[j]]=True
    
    # passes=passes[1:]

    # if False in passes:
    #     print("Oh, my keyboard!")

    # else:
    #     print("I become the guy.")

    n=int(input())

    coins=list(map(int,input().split()))
    coins=sorted(coins,reverse=True)

    total_coins=sum(coins)
    mid_coins=total_coins//2

    my_part=0
    coins_to_take=0

    for i in range(len(coins)):

        if my_part<=mid_coins:

            my_part+=coins[i]
            coins_to_take+=1

    print(coins_to_take)




        

