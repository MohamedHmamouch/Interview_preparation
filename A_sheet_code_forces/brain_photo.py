

if __name__=='__main__':

    n,m=map(int,input().split())
    colors=["C","M",'Y','W','G','B']
    black_white=True

    for _ in range(n):

        l=list(map(str,input().split()))

        if "C" in l or 'M' in l or 'Y' in l:

            black_white=False

    if black_white:
        print("#Black&White")

    else:

        print("#Color")


    