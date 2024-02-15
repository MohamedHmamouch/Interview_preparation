



if __name__=='__main__':

    n, m, k, t = map(int, input().split())
    ans = 0
    wasted = []
    for _ in range(k):
        a, b = map(int, input().split())
        wasted.append((a, b))

    wasted.sort()

    for _ in range(t):
        i, j = map(int, input().split())
        if (i, j) in wasted:
            print('Waste')
            continue
        else:
            g = (wasted + [(i, j)])
            g.sort()
            x = g.index((i, j))
            ans = (m*(i-1) + j) - x
            print('Carrots' if ans%3 == 1 else 'Kiwis' if ans%3 == 2 else 'Grapes')
    
    # n, m, k, t = map(int, input().split())
    # waste_pos = []
    # plants = ["Carrots", "Kiwis", "Grapes"]

    # for _ in range(k):
    #     a, b = map(int, input().split())
    #     a -= 1
    #     b -= 1
    #     waste_pos.append(m * a + b)

    # for _ in range(t):
    #     i, j = map(int, input().split())
    #     i -= 1
    #     j -= 1
    #     pos = m * i + j

    #     waste_before_cell = 0
    #     is_waste = False
    #     for p in waste_pos:
    #         if p == pos:
    #             is_waste = True
    #             break
    #         elif p < pos:
    #             waste_before_cell += 1

    #     if is_waste:
    #         print("Waste")
    #     else:
    #         print(plants[(pos - waste_before_cell) % 3])


    

