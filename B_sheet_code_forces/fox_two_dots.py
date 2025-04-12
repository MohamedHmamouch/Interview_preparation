if __name__ == '__main__':
    n, m = map(int, input().split())

    mat = []

    for i in range(n):
        mat.append(list(input()))

    def dfs(mat):
        
        visited=set()
        for i in range(n):
            for j in range(m):

                if (i,j) in visited:
                    continue

                color = mat[i][j]
                stack = [(i, j,-1,-1)]

                while stack:
                    x, y,px,py = stack.pop()

                    if (x, y) in visited:
                        return True
      
                    visited.add((x, y))
                    
                    move = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]

                    for node in move:
                        if 0 <= node[0] < n and 0 <= node[1] < m:
                            if mat[node[0]][node[1]] == color and (node[0],node[1]) != (px, py):
                                stack.append((node[0], node[1],x,y))

        return False

    if dfs(mat):

        print("YES")
    else:
        print("NO")
