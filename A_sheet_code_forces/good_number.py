


if __name__=='__main__':

    # Input
    # n, k = map(int, input().split())
    # not_good = 0

    # for _ in range(n):
    #     num = int(input())
    #     digits = set(str(num))

    #     for i in range(k + 1):
    #         if str(i) not in digits:
    #             not_good += 1
    #             break

    # print(n - not_good)


    #==================================================#

    n, k = map(int, input().split())

    digits=[i for i in range(k+1)]

    not_good=0

    for i in  range(n):

        num=int(input())
        nums_list=[int(x) for x in str(num)]

        for i in digits:

            if i not in nums_list:

                not_good+=1
                break
    print(n-not_good)








