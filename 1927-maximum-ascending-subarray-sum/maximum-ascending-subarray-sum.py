class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        total=nums[0]


        max_total=0
        for r in range(1,len(nums)):

            if nums[r]>nums[r-1]:

                total+=nums[r]
            
                max_total=max(total,max_total)

            else:
                max_total=max(total,max_total)

                total=nums[r]

        return max(max_total,total)