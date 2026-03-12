class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l,r=0,0

        total=0

        min_subarray=float('inf')
        while r<len(nums):

            total+=nums[r]

            while l<=r and total>=target:

                min_subarray=min(r-l+1,min_subarray)

                total-=nums[l]
                l+=1

            r+=1

        return min_subarray if min_subarray!=float('inf') else 0
        