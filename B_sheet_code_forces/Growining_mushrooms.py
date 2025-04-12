

if __name__=='__main__':
        
    n, t1, t2, k = map(int, input().split())


    classement = []
    percent=100-k

    for i in range(n):
        v1,v2=map(int,input().split())

        height_v1 = v1 * t1 * (percent/100) + v2 * t2
        height_v2 = v2 * t1 * (percent/100) + v1 * t2

        final_height = max(round(height_v1, 2), round(height_v2, 2))
        classement.append((i, final_height))

    classement.sort(key=lambda x: float(x[1]), reverse=True)

    for dwarf, height in classement:
        print(f"{dwarf+1} {height:.2f}")
