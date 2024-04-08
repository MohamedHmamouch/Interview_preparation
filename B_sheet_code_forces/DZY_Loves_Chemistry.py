


if __name__=='__main__':

    n,m=map(int,input().split())

    from collections import defaultdict
    graph=defaultdict(list)

    for i in range(m):
        
        x,y=map(int,input().split())
        root=x
        graph[x].append(y)
        graph[y].append(x)

    def dfs(start):
        visited[start]=True
        danger=1

        for neighbor in graph[start]:

            if not visited[neighbor]:

                danger*=2
                danger*=dfs(neighbor)

        return danger

    visited = [False] * (n + 1)
    ans = 1
    for i in range(1, n + 1):
        if not visited[i]:
            ans *= dfs(i)
    
    print(ans)



    