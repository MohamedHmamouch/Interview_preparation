class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()


        l=0
        r=len(nums)-1

        max_sum=-1

        while l<r:

            if nums[r]+nums[l]<k:
                max_sum=max(max_sum,nums[r]+nums[l])
                l+=1


            else:

                r-=1

        return max_sum
