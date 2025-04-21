def upper_bound(tops, x):
    # Recherche binaire : première position où tops[i] > x
    l, r = 0, len(tops)
    while l < r:
        mid = (l + r) // 2
        if tops[mid] > x:
            r = mid
        else:
            l = mid + 1
    return l

def main():
    n = int(input())
    cubes = list(map(int, input().split()))

    tops = []  # Représente les sommets des tours

    for cube in cubes:
        idx = upper_bound(tops, cube)

        if idx == len(tops):
            # Pas de tour où poser le cube → nouvelle tour
            tops.append(cube)
        else:
            # On pose le cube sur la tour idx
            tops[idx] = cube

    print(len(tops))

if __name__ == "__main__":
    main()
