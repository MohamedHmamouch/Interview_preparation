class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        s_dict={}

        for char in s:

            s_dict[char]=1+s_dict.get(char,0)

        
        t_dict={}
        for t_char in t:

            t_dict[t_char]=1+t_dict.get(t_char,0)

        
        if len(s_dict)!=len(t_dict): return False


        for char in s:

            if char not in t_dict or (char in t_dict and t_dict[char]!=s_dict[char]):

                return False

        return True