class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        left=0
        right=0
        res=0
        count_zeros=0
        while right<len(nums):

            count_zeros+=1 if nums[right]==0 else 0

            while left<=right and count_zeros>0:

                count_zeros-=1 if nums[left]==0 else 0

                left+=1

            res=max(res,right-left+1)

            right+=1

        return res

