class Solution:
    def maxSum(self, nums: List[int]) -> int:

        seen=set()

        current_sum=0

        max_total=float('-inf')

        for k in nums:

            if k not in seen:

                seen.add(k)

                if k>=0:
                    current_sum+=k

            
            max_total=max(max_total,current_sum)

        return max_total if max_total>0 else max(nums)