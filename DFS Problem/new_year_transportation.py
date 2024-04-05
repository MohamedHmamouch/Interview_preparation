from collections import defaultdict

def dfs(start, target, portals):
    visited = set()
    stack = [start]

    while stack:
        current_cell = stack.pop()
        if current_cell == target:
            return True
        if current_cell in visited:
            continue
        visited.add(current_cell)
        for next_cell in portals[current_cell]:
            stack.append(next_cell)

    return False

if __name__ == '__main__':
    n, t = map(int, input().split())
    cells = list(map(int, input().split()))
    portals = defaultdict(list)

    for i in range(len(cells)):
        portals[i + 1].append(i + 1 + cells[i])

    if dfs(1, t, portals):
        print("YES")
    else:
        print("NO")
