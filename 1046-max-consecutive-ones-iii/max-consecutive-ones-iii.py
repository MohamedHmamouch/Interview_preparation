class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:



        num_ones=0
        num_zeros=0

        max_subarray=0

        l,r=0,0

        while r<len(nums):


            num_ones+=1 if nums[r]==1 else 0

            num_zeros+=1 if nums[r]==0 else 0

            while l<r and num_zeros>k:

                num_ones-=1 if nums[l]==1 else 0

                num_zeros-=1 if nums[l]==0 else 0

                l+=1
            if num_zeros<=k:
                max_subarray=max(r-l+1,max_subarray)

            r+=1

        return max_subarray        