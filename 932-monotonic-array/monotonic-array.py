class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing_count=1
        decreasing_count=1

        equal=0
        l=r=0

        for r in range(1,len(nums)):

            if nums[r-1]<nums[r]:

                increasing_count+=1

            elif nums[r-1]>nums[r]:

                decreasing_count+=1

            else: equal+=1

        print(decreasing_count)
        print(increasing_count)
        print(equal)

        
        return True if (increasing_count+equal==len(nums) or decreasing_count+equal==len(nums)) else False