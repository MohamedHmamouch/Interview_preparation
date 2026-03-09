class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums)==1:

            return 0


        last_element=float('inf')

        for i in range(len(nums)):

            next_element=nums[i+1] if i+1<len(nums) else float('-inf')

            prev_element=nums[i-1] if i-1>=0 else float('-inf')

            
            if prev_element<nums[i]>next_element:return i


        