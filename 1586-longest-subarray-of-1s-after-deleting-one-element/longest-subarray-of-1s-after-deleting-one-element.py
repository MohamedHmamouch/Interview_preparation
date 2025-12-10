class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        total=0

        one_zero=0

        max_total=0

        l,r=0,0

        while r<len(nums):

            total+=nums[r]

            one_zero+=1 if nums[r]==0 else 0

            while l<r and one_zero>1:


                if nums[l]==0:

                    one_zero-=1

                l+=1

            if one_zero<=1:

                max_total=max(r-l+1-one_zero,max_total)

            r+=1

        return max_total if max_total!=len(nums) else max_total-1