class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        s=set()

        for n in nums:

            if n not in s:

                s.add(n)

            else:

                return n 
