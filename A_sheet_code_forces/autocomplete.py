

if __name__=='__main__':

    s=input()
    n=int(input())
    count=0
    next_string=[]

    for _ in range(n):
        
        input_string=input()

        if input_string.startswith(s):
            count+=1
            next_string.append(input_string)

    # print(next_string)


    if count==0 or s in next_string:
        print(s)
        exit()


    else:

        min_string=next_string[0]

        for i in range(len(next_string)):

            if next_string[i]<min_string:
                min_string=next_string[i]

    print(min_string)