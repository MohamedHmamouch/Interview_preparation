
if __name__=='__main__':

    n,k=map(int,input().split())

    nums=list(map(int,input().split()))

    for i in range(n):

        if nums[i]<0:

            nums[i]*=-1
            k-=1

        if k<=0:
            break

    if k>0:
        if k%2!=0:

            nums.sort()
            nums[0]*=-1

    print(sum(nums))