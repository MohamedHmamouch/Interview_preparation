class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        set_num=set()

        for n in nums:

            if n in set_num: return n 

            else: set_num.add(n)