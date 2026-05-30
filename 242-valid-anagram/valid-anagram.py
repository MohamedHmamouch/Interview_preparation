class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        s_mapper={}
        t_mapper={}

        for char in s:

            s_mapper[char]=1+s_mapper.get(char,0)

        for char in t:

            if char not in s_mapper:

                return False

            t_mapper[char]=1+t_mapper.get(char,0)


        for k,v in s_mapper.items():

            if k not in t_mapper:

                return False

            elif k in t_mapper and t_mapper[k]!=v:

                return False

        return True
        