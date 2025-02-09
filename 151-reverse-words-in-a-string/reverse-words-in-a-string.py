class Solution:
    def reverseWords(self, s: str) -> str:

        if len(s)==1:

            return s

        list_string=list(s.split())
        #0(n)
        print(list_string)
        l,r=0,len(list_string)-1

        while l<=r:

            list_string[l],list_string[r]=list_string[r],list_string[l]

            r-=1
            l+=1

        return ' '.join(list_string)
        