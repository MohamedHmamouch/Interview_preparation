class Solution:
    def findPeakElement(self, nums: List[int]) -> int:


        peak=-1*float('inf')
        peak_index=0

        

        

        for i in range(len(nums)-1):

            temp=nums[i-1] if i>=1 else -1*float('inf')

            if nums[i]>=nums[i+1] and nums[i]>=temp and nums[i]>=peak:

                peak=nums[i]

                peak_index=i

        
        return len(nums)-1 if nums[len(nums)-1]>=peak else peak_index
        