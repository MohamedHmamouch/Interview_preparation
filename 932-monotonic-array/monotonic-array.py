class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        
        increasing=1
        decreasing=1

        equal=0

        for i in range(1,len(nums)):

            if nums[i]<nums[i-1]:

                increasing+=1


            elif nums[i]>nums[i-1]:

                decreasing+=1

            else:

                equal+=1


        total_increasing=increasing+equal

        total_descreasing=decreasing+equal

        return True if (total_increasing==len(nums) or total_descreasing==len(nums)) else False