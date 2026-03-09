class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:


        product=1

        l=0
        r=0
        ans=0

        while r<len(nums):

            product*=nums[r]

            while l<r and product>=k:

                product//=nums[l]

                l+=1

            
            ans+=r-l+1 if product<k else 0

            r+=1

        return ans


        