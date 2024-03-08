

if __name__=='__main__':

    x=int(input())

    bin_x_list=list(bin(x))[2:]

    if 2**(len(bin_x_list)-1)==x:

        print(1)

    else:

        counter_ones=bin_x_list.count('1')
        print(counter_ones)
        