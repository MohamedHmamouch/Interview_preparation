class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        l=0

        new_str=""

        for r in range(len(s)):


            if l<len(spaces) and r==spaces[l]:
                new_str+=" "

                new_str+=s[r]

                l+=1

            else:

                new_str+=s[r]

        return new_str