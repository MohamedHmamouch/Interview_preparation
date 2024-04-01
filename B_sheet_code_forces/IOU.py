

if __name__=='__main__':

    n,m=map(int,input().split())

    total_debts=0
    records={}

    for _ in range(m):

        a,b,c=map(int,input().split())
        total_debts+=c

        records[a]=c+records.get(a,0)
        records[b]=-c+records.get(b,0)
    to_give=0
    to_receive=0    

    for _,v in records.items():
        if v>0:
            to_receive+=v
        if v<0:
            to_give+=v
    # print(to_receive)
    # print(to_give)
    print(min(to_receive,total_debts))
