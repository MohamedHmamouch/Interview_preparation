class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        l,r=0,0
        freq={}

        n=len(s)
        max_rep=0
        res=0

        while r<n:

            freq[s[r]]=1+freq.get(s[r],0)

            while l<=r and freq[s[r]]>1:

                freq[s[l]]-=1

                if freq[s[l]]==0:

                    del freq[s[l]]


                l+=1

            res=max(res,len(freq))
            r+=1

        return res

        