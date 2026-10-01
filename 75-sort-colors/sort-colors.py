class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        freq={
            0:0,
            1:0,
            2:0
        }

        for n in nums:

            freq[n]=1+freq.get(n,0)

        p1=0
        for key,val in freq.items():

            while val>0 and p1<len(nums):

                nums[p1]=key
                p1+=1
                val-=1

                