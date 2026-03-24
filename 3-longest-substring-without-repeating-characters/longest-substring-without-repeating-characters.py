class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        freq={}

        l=0
        r=0
        res=0

        while r<len(s):

            freq[s[r]]=1+freq.get(s[r],0)

            while l<r and freq[s[r]]>1:

                freq[s[l]]-=1

                if freq[s[l]]<0:

                    del freq[s[l]]

                l+=1

            res=max(r-l+1,res)
            r+=1

        return res