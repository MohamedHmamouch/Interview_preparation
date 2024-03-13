

if __name__=='__main__':

    n=int(input())
    # print(n)
    # print(n%10)
    # print(n%100)
    # print("#########")
    # print(n//10)
    # print(n//100)

    if int(n)>=0:

        print(int(n))

    else:
        
        positive_n=n*(-1)
        second_digit_=(positive_n // 100) * 10 + (positive_n % 10)
        last_digit=positive_n//10

        print(max(-1*last_digit,-1*second_digit_))



