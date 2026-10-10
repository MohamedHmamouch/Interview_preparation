class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:


        left=0
        right=k-1

        unique=set()

        while right<len(s):

            unique.add(s[left:right+1])
            left+=1

            right+=1



        return len(unique)==2**k



