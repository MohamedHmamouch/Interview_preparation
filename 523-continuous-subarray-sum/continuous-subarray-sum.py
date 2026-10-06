class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:

        freq={0:-1}

        current=0

        for i,n in enumerate(nums):

            current+=n

            if current%k in freq and i-freq[current%k]>=2:

                return True


            freq[current%k]= min(i,freq[current%k]) if current%k in freq else i

        return False