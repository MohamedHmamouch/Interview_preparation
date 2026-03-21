class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:


        nums.sort()

        i,j=0,0

        while j<len(nums):

            if nums[j]>nums[i]:
                i+=1

            j+=1

        return i
        
        