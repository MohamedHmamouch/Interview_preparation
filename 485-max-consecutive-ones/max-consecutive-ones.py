class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total=0
        max_total=0

        for r in range(len(nums)):

            total+=nums[r]
            max_total=max(total,max_total)

            if nums[r]==0:

                total=0

        return max_total