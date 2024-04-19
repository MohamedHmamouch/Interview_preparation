if __name__ == '__main__':
    n, d = map(int, input().split())

    friendship = []

    for _ in range(n):
        m, s = map(int, input().split())
        friendship.append((m, s))

    friendship.sort(key=lambda x: x[0])  

    max_friendship=0
    total_friendship=0
    salary=0 
    l,r=0,0
    for r in range(n):

        total_friendship+=friendship[r][1]

        while friendship[r][0]-friendship[l][0]>=d:
            total_friendship-=friendship[l][1]
            l+=1

        max_friendship=max(max_friendship,total_friendship)
            



    print(max_friendship)
