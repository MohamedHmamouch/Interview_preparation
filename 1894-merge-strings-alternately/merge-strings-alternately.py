class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        p1,p2=0,0

        p1_next=True

        s=""


        while p1<len(word1) and p2<len(word2):

            if p1_next:

                s+=word1[p1]

                p1_next=False

                p1+=1

            else:

                s+=word2[p2]

                p1_next=True

                p2+=1

        while p1<len(word1):

            s+=word1[p1]
            p1+=1

        while p2<len(word2):

            s+=word2[p2]

            p2+=1

        return s



        