if __name__=='__main__':
    import math

    n, r, avg = map(int, input().split())

    scores = []
    total = 0
    for _ in range(n):
        a, b = map(int, input().split())
        scores.append([a, b])
        total += a

    current_avg = total / n
    
    if current_avg >= avg:
        print(0) 
        exit() 
    else:
        scores.sort(key=lambda x: x[1])
        
        point_needed=abs(total-avg*n)
        time,my_sum=0,0
        for i in range(n):

            time+=(r-scores[i][0])*scores[i][1]

            my_sum+=r-scores[i][0]

            if my_sum>=point_needed:

                time-=(my_sum-point_needed)*scores[i][1]
                break
    print(time)
