
if __name__=='__main__':
    # Step 1: Read inputs
    s = input()
    string = list(s)
    m = int(input())
    positions = list(map(int, input().split()))
    n=len(s)

    # Step 2 and 3: Perform transformations
    for a in positions:
        
        to_move=string[a-1:n-a+1][::-1]
        # print(string[:a-1])
        # print(to_move)
        # print(string[n-a+1::])

        string=string[:a-1]+to_move+string[n-a+1::]

    # Step 4: Output the final string
    print(''.join(string))
