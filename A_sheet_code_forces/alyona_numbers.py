


if __name__=='__main__':

    n, m = map(int, input().split())

    count = 0
    l = [0] * 5

    # Count remainders for numbers up to min(n, m)
    for i in range(1, min(n, m) + 1):
        remainder = i % 5
        l[remainder] += 1

    # Count remainders for numbers up to max(n, m)
    for j in range(1, max(n, m) + 1):
        remainder = j % 5
        count += l[(5 - remainder) % 5]

    print(count)

    # remainders={}

    # first_loop,second_loop=min(n,m),max(n,m)

    # for i in range(1,first_loop+1):
        
    #     remainders[i]=i%5
        
        
    # for k in range(1,second_loop+1):
        
    #     remainder=k%5
        
    #     for _,v in remainders.items():

    #         if v+remainder==0:
            
    #             count+=1
    # print(remainders)
    # print(count)
    
    
    
    