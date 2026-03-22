class Solution:
    def isIsomorphic(self, strs: str, string: str) -> bool:
        

        mapper_to_t={}

        mapper_to_s={}

        for s,t in zip(strs,string):

            if s in mapper_to_t and mapper_to_t[s]!=t:

                return False

            if t in mapper_to_s and mapper_to_s[t]!=s:

                return False

            mapper_to_t[s]=t
            mapper_to_s[t]=s

        return True