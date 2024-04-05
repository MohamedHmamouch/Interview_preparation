

if __name__ == '__main__':
    n, x0, y0 = map(int, input().split())

    pas = set()

    for _ in range(n):
        x, y = map(int, input().split())

        if x - x0 != 0:
            a = (y - y0) / (x - x0)
            b = y0 - a * x0
        else:
            a = float('inf')  
            b = x0  

        pas.add((a, b))

    print(len(pas))
