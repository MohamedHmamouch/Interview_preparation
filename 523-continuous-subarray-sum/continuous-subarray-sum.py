class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:



        remainder={0:-1}
        
        prefix=0

        for r in range(len(nums)):

            prefix+=nums[r]

            if prefix%k in remainder and r-remainder[prefix%k]>=2:

                return True

            remainder[prefix%k]=min(r,

                remainder.get(prefix%k,float('inf'))
            
                )

        return False