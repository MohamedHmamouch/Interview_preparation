

if __name__=='__main__':

    from collections import deque


    def min_path(n,m):

        q=deque([(n,0)])
        visited=set()

        min_presses=float('inf')

        while q:

            node,press=q.popleft()

 
            if node==m:

                return min(press,min_presses)
            

            if node<=m and 2*node not in visited:
                q.append((node*2,press+1))
                visited.add(2*node)

            if node-1>0 and (node-1) not in visited:

                q.append((node-1,press+1))
                visited.add(node-1)

        return -1
    
    n,m=map(int,input().split())

    print(min_path(n,m))