class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowel={"a","e","o","i","u"}
        

        count=0

        max_count=0

        l,r=0,0

        while r<len(s):

            count+=1 if s[r] in vowel else 0

            while l<r and r-l+1>k:

                count-=1 if s[l] in vowel else 0

                l+=1

            max_count=max(max_count,count)

            r+=1

        return max_count

        