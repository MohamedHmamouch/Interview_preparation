

if __name__=='__main__':

    n = int(input())
    will = list(map(int, input().split()))
    k = list(map(int, input().split()))
    will=will[1:]
    k=k[1:]

    passes = [False] * (n+1)  # Initialize with length n+1

    for i in range(len(will)):
        passes[will[i]] = True

    for j in range(len(k)):
        passes[k[j]] = True

    passes=passes[1:]

    if passes.count(False)== 0:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
