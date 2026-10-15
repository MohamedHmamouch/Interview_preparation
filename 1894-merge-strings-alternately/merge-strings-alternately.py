class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:


        p1=1

        p2=0

        s=word1[0]

        altern=True
        

        while p1<len(word1) and p2<len(word2):

            if altern:

                s+=word2[p2]

                altern=False

                p2+=1

            else:

                s+=word1[p1]

                altern=True

                p1+=1

        
        if p1<len(word1):

            s+=word1[p1:]

        elif p2<len(word2):

            s+=word2[p2:]

        return s