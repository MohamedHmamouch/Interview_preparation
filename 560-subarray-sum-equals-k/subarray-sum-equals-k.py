class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        freq={0:1}

        count=0

        curr=0

        for n in nums:

            curr+=n

            if curr-k in freq:

                count+=freq[curr-k]

            

            freq[curr]=1+freq.get(curr,0)

        return count