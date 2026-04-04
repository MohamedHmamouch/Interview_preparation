class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        max_sum=-1

        for i in range(len(nums)):

            current_sum=nums[i]

            for j in range(i+1,len(nums)):

                current_sum=nums[i]+nums[j]

                if current_sum<k:

                    max_sum=max(max_sum,current_sum)

        return max_sum