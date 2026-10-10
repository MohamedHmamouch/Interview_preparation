class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:


        if len(s)<len(p):
            return []

        res=[]

        l=0

        scount={}
        pcount={}
        for r in range(len(p)):

            scount[s[r]]=1+scount.get(s[r],0)

            pcount[p[r]]=1+pcount.get(p[r],0)


        if scount==pcount:

            res.append(l)

        l=0

        for r in range(len(p),len(s)):


            scount[s[r]]=1+scount.get(s[r],0)

            scount[s[l]]-=1

            if scount[s[l]]<=0:

                del scount[s[l]]

            
            l+=1

            if scount==pcount:

                res.append(l)

        return res