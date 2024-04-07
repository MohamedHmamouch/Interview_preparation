

if __name__=='__main__':

    t=int(input())

    for i in range(t):

        num_vertices,num_edges=map(int,input().split())
        graph={}
        for _ in range(num_edges):

            x,y=map(int,input().split())

            graph[x]=1+graph.get(x,0)
            graph[y]=1+graph.get(y,0)

        count=0

        for k,v in graph.items():

            if v==1:
                count+=1

        num_vertices=num_vertices-count-1
        print(num_vertices,count//num_vertices)

            

        