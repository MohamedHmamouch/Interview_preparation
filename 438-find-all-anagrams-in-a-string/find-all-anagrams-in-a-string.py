class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        if len(p)>len(s):

            return []
        p_freq={}
        s_freq={}

        for i in range(len(p)):
            p_freq[p[i]]=1+p_freq.get(p[i],0)

            s_freq[s[i]]=1+s_freq.get(s[i],0)

        ans=[]

        if s_freq==p_freq:

            ans.append(0)

        end=len(p)
        start=0


        while end<len(s):

            s_freq[s[end]]=1+s_freq.get(s[end],0)
            s_freq[s[start]]-=1


            if s_freq[s[start]]<=0:

                del s_freq[s[start]]

            start+=1
            if s_freq==p_freq:

                ans.append(start)

            end+=1

        print(s_freq,p_freq)

        return ans