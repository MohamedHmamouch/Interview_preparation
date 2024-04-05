
def dfs(start,graph):

    stack=[start]

    path=0

    while stack:

        node=stack.pop()

        if node=="polycrap":
            return path

        else:
            path+=1

        for next in graph[node]:

            stack.append(next)

    return path

if __name__=='__main__':

    n=int(input())
    from collections import defaultdict
    graph=defaultdict(list)

    for _ in range(n):

        s=list(map(str,input().split()))

        graph[s[0].lower()].append(s[2].lower())

    maxi=0

    for k in list(graph.keys()):

        maxi=max(maxi,dfs(k,graph))

    print(maxi)


