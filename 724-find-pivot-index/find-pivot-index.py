class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        total=sum(nums)

        current_sum=0


        for r in range(len(nums)):


            current_sum+=nums[r]

            if total==current_sum:

                return r

            total-=nums[r]

        return -1
        