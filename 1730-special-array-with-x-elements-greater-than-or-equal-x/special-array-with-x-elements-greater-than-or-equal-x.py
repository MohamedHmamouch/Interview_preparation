class Solution:
    def specialArray(self, nums: list[int]) -> int:
        
        
        freq={}

        for val in range(1,1001):

            for num in nums:

                if num>=val:

                    freq[val]=1+freq.get(val,0)

        

        for k,v in freq.items():

            if k==v:return k
        return -1