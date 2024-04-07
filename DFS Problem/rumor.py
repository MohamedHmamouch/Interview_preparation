def dfs(start):

    stack=[start]

    cost=gold[start-1]

    visited[start]=True

    while stack:

        node=stack.pop()

        for next_node in graph[node]:

            if visited[next_node]:

                continue

            cost=min(cost,gold[next_node-1])
            stack.append(next_node)
            visited[next_node]=True
    return cost

if __name__=='__main__':

    n,m=map(int,input().split())

    gold=list(map(int,input().split()))


    from collections import defaultdict
    
    graph=defaultdict(list)

    for _ in range(m):

        x,y=map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited=[False]*(n+1)

    ans=0

    for i in range(1,n+1):

        if not visited[i]:

            ans+=dfs(i)

    for i in range(1,n+1):

        if not visited[i]:
            ans+=gold[i-1]

    print(ans)

