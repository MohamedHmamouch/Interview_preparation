

if __name__=='__main__':

    n,s=map(int,input().split())

    steps=[]

    for _ in range(n):

        steps.append(list(map(int,input().split())))

    steps.sort(key=lambda x:x[0],reverse=True)
    
    time_take=0


    for i in range(len(steps)):

        floor=steps[i][0]
        time_take+=abs(floor-s)
        s=floor
        if time_take<steps[i][1]:
            time_take+=abs(steps[i][1]-time_take)

    while s!=0:

        time_take+=1
        s-=1

    print(time_take)

        