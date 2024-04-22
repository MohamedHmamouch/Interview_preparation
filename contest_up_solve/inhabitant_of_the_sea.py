if __name__=='__main__':
# 6
# 4 5
# 1 2 4 3
# 4 6
# 1 2 4 3
# 5 20
# 2 7 1 8 2
# 2 2
# 3 2
# 2 15
# 1 5
# 2 7
# 5 2


# T = int(input())
# for _ in range(T):

#     sinked=0
#     n,k= map(int, input().split())
#     a=[int(i) for i in input().split()]

#     for hit in range(0,k):
#         if 0 in a:
#             a.remove(0)
#             sinked+=1

#         if a==list():
#             break

#         if hit%2==0:
#             a[0]-=1
#         else:
#             a[-1]-=1

#     if 0 in a:
#             a.remove(0)
#             sinked+=1
            
#     print(sinked)


#TOOOOOOO SLOOOOOOOOOOOOOOOOOOOOOOOOOOOW

    T = int(input())
    for _ in range(T):

        sinked=0
        n,k= map(int, input().split())
        a=[int(i) for i in input().split()]
        dead=[0 for i in range(0,n)]
        rear=k//2
        frontal=k-rear

        
        for i in range(0,len(a)):
            if frontal>=a[i]:
                frontal-=a[i]
                a[i]=0
            else:
                a[i]-=frontal
                frontal=0
            

        for i in range(-1,-len(a)-1,-1):
            
            if rear>=a[i]:
                rear-=a[i]
                a[i]=0
            else:
                a[i]-=rear
                rear=0

            
        
        print(a.count(0))


        
