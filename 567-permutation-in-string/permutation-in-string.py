class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        
        ord_s1=[0]*26
        ord_s2=[0]*26

        n1=len(s1)
        n2=len(s2)

        if n1>n2:

            return False


        for i in range(len(s1)):

            ord_s1[ord(s1[i])-ord('a')]+=1

            ord_s2[ord(s2[i])-ord('a')]+=1

        if ord_s1==ord_s2:

            return True


        
        for k in range(n1,n2):

            ord_s2[ord(s2[k])-ord('a')]+=1

            ord_s2[ord(s2[abs(k-n1)])-ord('a')]-=1


            if ord_s2==ord_s1:

                return True

        return False

