class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        l,r=0,0
        res=float('inf')
        total=0

        while r<len(nums):

            total+=nums[r]

            while total>=target:
                res=min(r-l+1,res)
                total-=nums[l]
                l+=1



            r+=1

        return res if res!=float('inf') else 0



        