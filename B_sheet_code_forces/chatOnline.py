


if __name__=='__main__':


    p,q,l,r=map(int,input().split())

    time_Z={}

    for _ in range(p):

        a,b=map(int,input().split())

        time_Z[a]=b

    count_interval=[]


    for _ in range(q):

        a,b=map(int,input().split())

        for t in range(l,r+1):

            c=a+t
            d=b+t


            for min_time,max_time in time_Z.items():

                if d>=min_time and c<=max_time:
                    if t not in count_interval:
                        count_interval.append(t)



    print(len(count_interval))

        