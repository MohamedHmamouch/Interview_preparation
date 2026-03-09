class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        l=0
        r=0

        total=0

        min_length=float('inf')

        while r<len(nums):

            total+=nums[r]

            while l<=r and total>=target:

                min_length=min(min_length,r-l+1)

                total-=nums[l]

                l+=1

            r+=1

        return min_length if min_length!=float('inf') else 0

                