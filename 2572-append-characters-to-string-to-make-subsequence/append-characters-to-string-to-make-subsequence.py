class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        # idea: t is a subsequence of s if we can remove some char from s and have t while keeping the same order
        # the idea is to look for char that are similar keep them and add those are not. 
        # if i know the number of char that are similar i need to add only t-number of smilar char

        i,j=0,0

        n=len(s)

        count=0

        while j<len(t) and i<len(s):

            if s[i]==t[j]:

                i+=1
                j+=1
                count+=1

            else:

                i+=1

        return len(t)-count

            