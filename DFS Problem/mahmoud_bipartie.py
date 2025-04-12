def dfs(start,graph):

    stack=[start]

    set1=set()
    set2=set()

    while stack:

        node=stack.pop()

        set1.add(node)

        for next_node in graph[node]:

            set2.add(next_node)
            stack.append(next_node)
    return [set1,set2]

        



if __name__=='__main__':

    n=int(input())
    from collections import defaultdict
    graph=defaultdict(list)

    for _ in range(n-1):

        x,y=map(int,input().split())

        graph[x].append(y)
        graph[y].append(x)

    set1,set2=dfs(1,graph=graph)
    print(set1,set2)

    

