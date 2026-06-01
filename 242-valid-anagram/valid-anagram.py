class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):

            return False

        s_to_t={}

        for char in s:

            s_to_t[char]=1+s_to_t.get(char,0)

        
        for char in t:


            if char not in s_to_t:

                return False


            s_to_t[char]-=1

            if s_to_t[char]<0:

                return False

        return True