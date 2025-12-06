class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:



        current_max=0

        for k in range(len(nums)):

            current_max=max(current_max,nums[k])

            nums[k]=nums[k]+current_max


        
        for k in range(1,len(nums)):

            nums[k]+=nums[k-1]

        return nums