class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        seen={}

        for n in nums:

            seen[n]=1+seen.get(n,0)

        

        for k,v in seen.items():

            if v==1:

                return k 
        