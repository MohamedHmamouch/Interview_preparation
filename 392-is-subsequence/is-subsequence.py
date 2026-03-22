class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        res=""

        p1=0
        p2=0

        num_char_s=sum([1 for char in s])
        num_char_t=sum([1 for char in t])

        print(num_char_s,num_char_t)

        while p1<num_char_s and p2<num_char_t:

            if s[p1]==t[p2]:

                res+=s[p1]
                p1+=1
                p2+=1

            else:

                p2+=1

        print(s)
        print(res)
        return s==res

