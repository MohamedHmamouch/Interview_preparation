    

if __name__=='__main__':
    n, m, k = map(int, input().split())
    holes = set(map(int, input().split()))

    bone_coordinate = 1

    for _ in range(k):
        x, y = map(int, input().split())

        if bone_coordinate in holes:
            break
        if x == bone_coordinate:
            bone_coordinate = y
        elif y == bone_coordinate:
            bone_coordinate = x


    print(bone_coordinate)
