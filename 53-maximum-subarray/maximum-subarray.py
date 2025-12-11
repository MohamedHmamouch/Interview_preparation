class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        max_sum=float('-inf')


        total=0

        for k in nums:

            if total+k>=0:

                total+=k
                max_sum=max(max_sum,total)

            else:

                total=0



        return max_sum if max_sum!=float('-inf') else max(nums)