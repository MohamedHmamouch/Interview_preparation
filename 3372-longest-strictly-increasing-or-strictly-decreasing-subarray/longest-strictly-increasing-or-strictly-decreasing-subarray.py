class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        increasing=1
        decreasing=1
        count=1

        for r in range(1,len(nums)):


            if nums[r]>nums[r-1]:

                increasing+=1
                decreasing=1

            elif nums[r]<nums[r-1]:

                decreasing+=1
                increasing=1

            else:

                increasing=1
                decreasing=1

            count=max(increasing,decreasing,count)

        return count

