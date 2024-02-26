

if __name__=='__main__':


    n,m=map(int,input().split())
    next_prime=0

    if n==2 and m==3:

        print("Yes")

    
    else:

        for i in range(n+1,m+1):
            div=[]


            for j in range(1,i+1):

                if i%j==0:

                    div.append(j)
                # print(f"this list {div} is for j: {j} and {i}")

            if len(div)==2 and 1 in div and i in div:
                next_prime=j
                break

    if next_prime==m:
        print("YES")
    else:

        print("NO")