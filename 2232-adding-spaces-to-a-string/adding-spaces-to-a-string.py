class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:

        p1=0
        p2=0

        new_str=""
        

        while p2<len(spaces):

            if p1==spaces[p2]:

                new_str+=" "

                p2+=1

            else:

                new_str+=s[p1]

                p1+=1

        while p1<len(s):

            new_str+=s[p1]

            p1+=1
            
        return new_str