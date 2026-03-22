class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        s=s.split()

        return sum([1 for char in s[-1]])
        