class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        if len(s)<10:

            return []

        
        left,right=0,9

        ans=set()
        freq={s[left:right+1]:1}

        # AAAAACCCCC

        while right+1<len(s):

            left+=1

            right+=1

            current=s[left:right+1]

            if current in freq:

                ans.add(current)

            freq[current]=1+freq.get(current,0)

        return list(ans)
        