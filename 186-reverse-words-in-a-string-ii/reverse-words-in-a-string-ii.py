class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        

        s.reverse()

        l=0

        for r in range(len(s)):

            if s[r]==" ":

                start=l
                end=r-1

                while start<end:

                    s[start],s[end]=s[end],s[start]

                    start+=1

                    end-=1

                l=r+1


        start=l
        end=r

        while l<r:

            s[l],s[r]=s[r],s[l]

            r-=1

            l+=1
            