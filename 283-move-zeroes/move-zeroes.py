class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0

        for r in range(len(nums)):

            if nums[r]!=0:

                nums[left],nums[r]=nums[r],nums[left]
                left+=1