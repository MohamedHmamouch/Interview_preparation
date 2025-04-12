


if __name__ == "__main__":

    n=int(input())
    nums=list(map(int,input().split()))

    left=0
    max_len=0

    freq={}

    for r in range(n):

        if nums[r] in freq:

            freq[nums[r]]+=1

        else:

            freq[nums[r]]=1

        while max(freq.keys())-min(freq.keys())>1:


            freq[nums[left]]-=1


            if freq[nums[left]]==0:

                del freq[nums[left]]

            left+=1

        max_len=max(max_len,r-left+1)

    print(max_len)

