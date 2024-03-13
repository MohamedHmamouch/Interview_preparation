


if __name__=='__main__':

    def maxi(x,m,w):

        return max(0.3*x,(1-(m/250))*x-50*w)
    
    score=[500,1000,1500,2000,2500]

    minutes=list(map(int,input().split()))
    wrong_submissions=list(map(int,input().split()))
    hacks=list(map(int,input().split()))

    total_score=0

    for x,w,m in zip(score,wrong_submissions,minutes):
        total_score+=maxi(x,m,w)


    total_score=total_score+100*hacks[0]-50*hacks[1]

    print(int(total_score))
