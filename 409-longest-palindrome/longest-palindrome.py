class Solution:
    def longestPalindrome(self, s: str) -> int:

        mapper={}

        for char in s:

            mapper[char]=1+mapper.get(char,0)

        


        longest=0
        is_odd=False

        for k,v in mapper.items():

            if v%2==0:

                longest+=v

            else:
                is_odd=True
                longest+=v-1
        
        return longest+1 if is_odd else longest