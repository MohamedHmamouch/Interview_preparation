class Solution:
    def largestNumber(self, nums: list[int]) -> str:


        if not any(map(bool,nums)):

            return "0"


        for i,n in enumerate(nums):

            nums[i]=str(n)
        

        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                left=nums[i]+nums[j]
                right=nums[j]+nums[i]

                if left+right<=right+left:

                    nums[i],nums[j]=nums[j],nums[i]

                

        return "".join(nums)