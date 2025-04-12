

if __name__=='__main__':

    t = int(input())
    for _ in range(t):
        n = int(input())
        sticks = list(map(int, input().split()))
        sticks.sort()
        polygons = 0
        i = 0
        while i < n:
            if i + 2 < n and sticks[i] + sticks[i+1] <= sticks[i+2]:
                polygons += 1
                i += 3
            else:
                i += 1
        print(polygons)
