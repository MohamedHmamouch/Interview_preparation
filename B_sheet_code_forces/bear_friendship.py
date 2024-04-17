
if __name__=='__main__':


    from collections import defaultdict

    n,m=map(int,input().split())

    graph=defaultdict(list)

    for _ in range(m):

        a,b=map(int,input().split())

        graph[a].append(b)
        graph[b].append(a)

    visited=[0]*(n+1)

    def bfs(start):

        """count number of node and edges"""

        q=set()
        q.add(start)

        visited[start]=1
        num_node=1
        num_edges=0

        while q:

            node=q.pop()

            if visited[node]==0:

                visited[node]=1

                num_node+=1

            for next_node in graph[node]:

                if visited[next_node]==0:

                    q.add(next_node)

                    num_edges+=1

        
        return num_edges,num_node
    

    is_reseanoble=True

    for i in graph.keys():

        if not visited[i]:

            num_edge,num_nodes=bfs(i)

            if num_edge!=(num_nodes*(num_nodes-1))//2:

                is_reseanoble=False
                break

    if is_reseanoble:
        print("YES")

    else:
        print("NO")

            























    # n,m = map(int,input().split())
    # c = {i:{i} for i in range(1,n+1)}
    # s = [1] * n
    # for i in range(m):
    #     x,y = map(int,input().split())
    #     c[x].add(y)
    #     c[y].add(x)
    # f = 1
    # for i in c:
    #     if s[i-1]:
    #         for j in c[i]:
    #             s[j-1] = 0
    #             if c[i] != c[j]: f = 0
    # print('YES') if f else print('NO')

    

                 