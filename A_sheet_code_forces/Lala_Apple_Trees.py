

if __name__=='__main__':

    n=int(input())
    l=[]
    
    left_trees=[]
    right_trees=[]

    for _ in range(n):

        tree=list(map(int,input().split()))
        if tree[0]>0:
            right_trees.append((tree[0],tree[1]))

        else:
            left_trees.append((-tree[0],tree[1]))

    right_trees.sort()
    left_trees.sort()

    res=0

    n_right_trees=len(right_trees)
    n_left_trees=len(left_trees)
    right_direction=True if n_right_trees>n_left_trees else False
    right_index=left_index=0
    
        

        