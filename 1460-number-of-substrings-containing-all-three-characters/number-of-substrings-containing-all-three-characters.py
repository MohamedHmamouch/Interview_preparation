class Solution:
    def numberOfSubstrings(self, s: str) -> int:


        l,r=0,0

        res=0

        freq={}
        n=len(s)

        while r<len(s):

            freq[s[r]]=1+freq.get(s[r],0)

            while len(freq)>=3:

                res+=n-r

                freq[s[l]]-=1

                if freq[s[l]]<=0:

                    del freq[s[l]]

                l+=1

            r+=1

        return res
        