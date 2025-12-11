class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:


        l,r=0,0

        max_total=0

        zeros=0
        total=0

        while r<len(nums):

            total+=nums[r]

            zeros+=1 if nums[r]==0 else 0

            while l<r and zeros>k:

                total-=nums[l]

                if nums[l]==0:

                    zeros-=1

                l+=1

            if zeros<=k:
                max_total=max(max_total,r-l+1)

            r+=1

        return max_total
        