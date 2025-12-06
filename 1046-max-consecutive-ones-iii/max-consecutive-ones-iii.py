class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:


        if k==0 and sum(nums)==0:

            return 0

        
        max_total=0

        current_total=0

        number_zeros=0

        l,r=0,0

        while r<len(nums):

            number_zeros+=1 if nums[r]==0 else 0

            if nums[r]==0: current_total+=1

            else:current_total+=1


            while l<r and number_zeros >k:

                current_total-=1

                if nums[l]==0:

                    number_zeros-=1

                l+=1

            max_total=max(max_total,current_total)

            r+=1

        return max_total
