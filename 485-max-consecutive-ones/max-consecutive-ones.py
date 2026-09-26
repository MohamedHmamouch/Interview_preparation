class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        

        total=0
        max_sum=float('-inf')


        for r in range(len(nums)):

            
            max_sum=max(max_sum,total)

            if nums[r]==0:

                total=0

            else:total+=nums[r] 

        return max(max_sum,total)