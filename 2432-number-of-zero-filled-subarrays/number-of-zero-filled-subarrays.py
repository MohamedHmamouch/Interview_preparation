class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:

        left=0
        right=0

        n=len(nums)

        count=0
        
        while right<n:

            if nums[right]==0:
                left=right

                while right<n and nums[right]==0:

                    count+=right-left+1

                    right+=1

            else:

                right+=1

        return count