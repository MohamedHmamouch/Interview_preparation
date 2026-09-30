class Solution:
    def longestPalindrome(self, s: str) -> int:


        freq={}
        

        for char in s:

            freq[char]=1+freq.get(char,0)

        

        ans=0

        odd=False

        for k,v in freq.items():

            if v%2==0:ans+=v

            else:

                odd=True
                ans+=v-1

        return ans+1 if odd else ans