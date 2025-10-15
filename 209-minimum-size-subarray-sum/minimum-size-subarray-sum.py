class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        total=0
        min_subarray=float('inf')

        l=0
        r=0


        while r<len(nums):

            total+=nums[r]

            while l<=r and total>=target:

                total-=nums[l]

                min_subarray=min(r-l+1,min_subarray)

                l+=1

            r+=1

        return 0 if min_subarray==float('inf') else min_subarray

            


        