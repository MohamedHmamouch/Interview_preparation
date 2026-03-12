class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:


        l,r=0,0

        num_ones=0

        num_zeros=0
        total=0
        while r<len(nums):

            num_zeros+=1 if nums[r]==0 else 0

            num_ones+=1 if nums[r]==1 else 0

            while l<=r and num_zeros>k:

                if nums[l]==0:

                    num_zeros-=1

                l+=1

            
            if num_zeros<=k:

                total=max(total,r-l+1)

            r+=1

        return total