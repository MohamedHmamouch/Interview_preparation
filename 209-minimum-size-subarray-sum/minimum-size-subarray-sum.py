class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        res=float('inf')

        left,right=0,0
        total=0

        while right<len(nums):
            
            total+=nums[right]

            while left<=right and total>=target:

                res=min(res,right-left+1)

                total-=nums[left]

                left+=1

            right+=1

        return res if res!=float('inf') else 0
