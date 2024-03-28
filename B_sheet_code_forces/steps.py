

if __name__=='__main__':

    n, m = map(int, input().split())
    xc, yc = map(int, input().split())
    k = int(input())

    total_steps = 0

    for _ in range(k):
        dx, dy = map(int, input().split())
        max_steps = float('inf')
        if dx > 0:
            max_steps = min(max_steps, (n - xc) // dx)
        elif dx < 0:
            max_steps = min(max_steps, (xc - 1) // (-dx))
        if dy > 0:
            max_steps = min(max_steps, (m - yc) // dy)
        elif dy < 0:
            max_steps = min(max_steps, (yc - 1) // (-dy))
        total_steps += max_steps
        xc += max_steps * dx
        yc += max_steps * dy

    print(total_steps)






