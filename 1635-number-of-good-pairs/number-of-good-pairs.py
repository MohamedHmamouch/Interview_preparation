
import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        mapper={}

        for n in nums:

            mapper[n]=1+mapper.get(n,0)


        total=0

        for _,v in mapper.items():

            total+=math.comb(v,2)

        return total
        