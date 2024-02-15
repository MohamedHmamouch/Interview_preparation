

class Graph:

    def __init__(self):

        self.graph={}


    def addEdges(self,u,v):

        if u not in self.graph:

            self.graph[u]=[v]

        else:

            self.graph[u].append(v)

    def BFS(self,s):

       #s: starting node
        queue=[s]

        visited=[False]*len(self.graph)

        while len(queue)>0:

            node=queue.pop(0)

            print(node)
            visited[node]=True

            for n in self.graph[node]:
                
                if visited[n]==False:

                    queue.append(n)
                    visited[n]=True

    def DFS(self,s):

       #s: starting node
        stack=[s]

        visited=[False]*len(self.graph)

        while len(stack)>0:

            node=stack.pop()

            print(node)
            visited[node]=True

            for n in self.graph[node]:
                
                if visited[n]==False:

                    stack.append(n)
                    visited[n]=True

if __name__=='__main__':

    g=Graph()
    g.addEdges(0,1)
    g.addEdges(0,2)
    g.addEdges(0,3)
    g.addEdges(1,4)
    g.addEdges(2,3)
    g.addEdges(3,4)
    g.addEdges(3,5)
    g.addEdges(4,0)
    g.addEdges(5,2)
    g.BFS(0)


