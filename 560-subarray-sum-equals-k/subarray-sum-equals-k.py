class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        mapper={0:1}

        prefix=0

        count=0

        for i,n in enumerate(nums):

            prefix+=n 
            count+=mapper.get(prefix-k,0)
            mapper[prefix]=1+mapper.get(prefix,0)

        return count


        