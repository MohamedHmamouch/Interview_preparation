from collections import deque

def bfs(start):
    visited = set()
    min_operations = float('inf')  # Initialize array for memoization
    queue =deque([(start, 0)])
    
    while queue:
        node, level = queue.popleft()

        if node==0:

            return min(level,min_operations)
        
        val=(node + 1) % 32768

        if val not in visited:
            visited.add(val)
            queue.append((val, level + 1))
        if (2 * node) % 32768 not in visited:
            val = (2 * node) % 32768
            queue.append((val, level + 1))

if __name__ == '__main__':
    n = int(input())
    integers = list(map(int, input().split()))
    
    for i in integers:
        print(bfs(i), end=" ")
