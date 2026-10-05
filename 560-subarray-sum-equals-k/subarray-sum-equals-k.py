class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        freq={0:1}

        current_sum=0

        count=0

        for n in nums:

            current_sum+=n

            if current_sum-k in freq:

                count+=freq.get(current_sum-k ,0)

            freq[current_sum]=1+freq.get(current_sum,0)

        return count