class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        l,r=0,0

        l1=[0]*26
        l2=[0]*26

        for char in s1:

            l1[ord(char)-ord('a')]+=1



        while r<len(s2):

            l2[ord(s2[r])-ord('a')]+=1

            while r-l+1>=len(s1):

                if l2==l1:

                    return True

                else:

                    l2[ord(s2[l])-ord('a')]-=1

                    if l2[ord(s2[l])-ord('a')]<0:
                        l2[ord(s2[l])-ord('a')]=0

                l+=1

            r+=1
        return False

                        