class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:



        hash_map={0:-1}

        prefix=0
        for i, n in enumerate(nums):

            prefix+=n

            remainder=prefix%k

            if remainder in hash_map:

                if i-hash_map[remainder]>=2:

                    return True
            else:
                hash_map[remainder]=i

        return False