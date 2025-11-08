class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        l=0
        r=1
        max_price=0


        while  r<len(nums):


            if nums[r]>nums[l]:

                max_price=max(max_price,nums[r]-nums[l])

            else:

                l=r

                # r+=1

                # if r<len(nums) and nums[r]-nums[l]>=max_price:

                #     max_price=nums[r]-nums[l]

                
            r+=1

        return max_price