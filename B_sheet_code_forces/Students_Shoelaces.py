


if __name__=='__main__':

    n,m=map(int,input().split())
    from collections import defaultdict

    graph=defaultdict(list)

    for _ in range(m):

        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # ones = set()
    
    flag=True
    groups=0

    while flag:

        l=[]

        flag=False

        for i in graph.keys():

            if len(graph[i])==1:

                l.append(i)
                flag=True

        
        if flag:

            groups+=1

            for i in l:

                del graph[i]

            for i in graph.keys():

                for j in l:

                    if j in graph[i]:

                        graph[i].remove(j)

    print(groups)

