class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:


        l,r=0,0

        number_contiguous=0

        current_product=1

        while r<len(nums):

            current_product*=nums[r]

            while l<=r and current_product>=k:

                current_product/=nums[l]

                l+=1

            
            if current_product<k:

                number_contiguous+=r-l+1

            r+=1

        return number_contiguous
        