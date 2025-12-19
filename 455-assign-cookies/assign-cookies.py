class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        

        g.sort()
        s.sort()

        greed=0
        size=0

        count=0

        while greed<len(g) and size<len(s):


            if g[greed]<=s[size]:

                count+=1
                greed+=1
                size+=1

            elif g[greed]>s[size]:

                size+=1

        return count