class Solution:
    def maxSum(self, nums: List[int]) -> int:
        

        seen=set()

        total=0
        max_total=0

        for k in nums:

            if k not in seen:

                seen.add(k)

                if k>=0:
                    
                    total+=k

            max_total=max(max_total,total)

        
        return max_total if max_total>0 else max(nums)