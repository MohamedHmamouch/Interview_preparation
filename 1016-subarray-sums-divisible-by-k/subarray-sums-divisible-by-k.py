class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        freq={0:1}

        prefix=0

        count=0

        for n in nums:

            prefix+=n

            remainder=prefix%k

            count+=freq.get(remainder,0)

            freq[remainder]=1+freq.get(remainder,0)

        return count