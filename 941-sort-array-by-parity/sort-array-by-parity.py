class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        

        left,right=0,0

        for right in range(len(nums)):

            if nums[right]%2==0 and nums[left]%2!=0:

                nums[left],nums[right]=nums[right],nums[left]

                left+=1

            elif nums[left]%2==0:

                left+=1

        return nums