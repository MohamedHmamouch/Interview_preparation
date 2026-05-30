class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        freq={}

        left,right=0,0

        res=0

        while right<len(s):

            freq[s[right]]=1+freq.get(s[right],0)

            while left<=right and freq[s[right]]>1:

                freq[s[left]]-=1

                if freq[s[left]]<=0:

                    del freq[s[left]]

                left+=1

            res=max(res,right-left+1)

            right+=1

        return res

            
        