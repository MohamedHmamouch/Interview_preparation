class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:  

        if len(s)==1:

            return s[0]


        longest_prefix=""
        max_length=0

        for i in range(len(s[0])):

            strs=s[0][:i+1]

            count=0
            for j in range(1,len(s)):

                if strs==s[j][:i+1]:

                    count+=1

            
            if count==len(s)-1 and len(strs)>=max_length:

                max_length=len(strs)

                longest_prefix=strs

        return longest_prefix