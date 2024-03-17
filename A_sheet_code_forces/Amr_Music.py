

if __name__=='__main__':

    n,k=map(int,input().split())

    instruments=list(map(int,input().split()))

    index_instruments={}

    for i in range(len(instruments)):

        index_instruments[i+1]=instruments[i]

    index_instruments_sorted=dict(sorted(index_instruments.items(),key=lambda x: x[1]))
    nunmber_instruments=0
    count=0
    index_instru=[]

    for key,v in index_instruments_sorted.items():
        nunmber_instruments+=v

        if k>=nunmber_instruments:
            count+=1
            index_instru.append(key)

    print(count)
    for i in index_instru:
        print(i,end=" ")


    # instruments.sort()
    # nunmber_instruments=0
    # count=0
    # index_instru=[]

    # for i in range(len(instruments)):

    #     nunmber_instruments+=instruments[i]

    #     if k>=nunmber_instruments:
    #         count+=1
    #         index_instru.append(i+1)

    #     else:
    #         break

    # print(count)
    # for i in index_instru:
    #     print(i,end=' ')

