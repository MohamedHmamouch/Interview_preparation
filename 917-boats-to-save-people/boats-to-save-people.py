class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:

        nums.sort()

        l,r=0,len(nums)-1

        boat=0


        while l<=r:


            if nums[r]+nums[l]<=limit:

                boat+=1

                r-=1

                l+=1

            elif nums[r]+nums[l]>limit:

                boat+=1
                r-=1

        return boat