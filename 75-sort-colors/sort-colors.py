class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        freq={}

        for n in nums:

            freq[n]=1+freq.get(n,0)


        start=0
        end=len(nums)-1


        for k,v in freq.items():

            if k==2:

                while v>0:

                    nums[end]=k
                    end-=1
                    v-=1

            elif k==0:

                while v>0:

                    nums[start]=k
                    start+=1
                    v-=1

        print(nums)
        for i in range(start,end+1):

            nums[i]=1

        print(nums)