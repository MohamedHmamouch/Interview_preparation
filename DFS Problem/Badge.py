
def dfs(start,graph):

    stack=[start]
    visited=set()

    while stack:

        node=stack.pop()

        if node in visited:
            return node
        else:

            visited.add(node)

        for next_node in graph[node]:

            stack.append(next_node)

if __name__=='__main__':

    n=int(input())

    students=list(map(int,input().split()))
    from collections import defaultdict
    g=defaultdict(list)

    for i in range(len(students)):

        g[i+1].append(students[i])

    

    for key,val in g.items():
        print(dfs(key,graph=g),end=" ")