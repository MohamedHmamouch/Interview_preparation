class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        s_to_t={}

        t_to_s={}

        for i,j in zip(s,t):


            if i in s_to_t and s_to_t[i]!=j:

                return False

            s_to_t[i]=j
            t_to_s[j]=i

        
        print(s_to_t)

        print(t_to_s)

        for k,v in s_to_t.items():

            if k!=t_to_s[v]:

                return False

        return True