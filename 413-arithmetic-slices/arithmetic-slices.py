class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        if len(nums)<3:

            return 0

        l=0
        res=0
        diff=nums[1]-nums[0]

        for i in range(2,len(nums)):

            temp=l

            if nums[i]-nums[i-1]==diff:

                while i-l+1>=3:

                    res+=1
                    l+=1
                
                l=temp

            else:

                diff=nums[i]-nums[i-1]
                l=i-1

        return res