

if __name__=='__main__':

    n = int(input())

    forces=[]
    x_axis=0
    y_axis=0
    z_axis=0

    for _ in range(n):

        forces=list(map(int,input().split()))

        x_axis+=forces[0]
        y_axis+=forces[1]
        z_axis+=forces[2]

    if x_axis==0 and y_axis==0 and z_axis==0:
        print("YES")
    else:
        print("NO")




