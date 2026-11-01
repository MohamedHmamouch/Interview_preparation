class Solution:
    def countBadPairs(self, nums: list[int]) -> int:

        good_pairs=0
        length=len(nums)

        mapper={}

        for i,n in enumerate(nums):

            good_pairs+=mapper.get(i-n,0)

            mapper[i-n]=1+mapper.get(i-n,0)


        return length*(length-1)//2 -good_pairs
        