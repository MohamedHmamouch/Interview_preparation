class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l,r=0,0

        longest=0

        freq={}
        max_freq=0

        while r<len(s):
            
            freq[s[r]]=1+freq.get(s[r],0)

            max_freq=max(max_freq,freq[s[r]])

            while l<r and r-l+1-max_freq>k:

                freq[s[l]]-=1

                if freq[s[l]]<=0:

                    del freq[s[l]]

                l+=1

            
            longest=max(longest,r-l+1)

            r+=1

        return longest