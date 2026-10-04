class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        even=0

        even_prefix=0

        odd_prefix=0

        mod=10**9 + 7

        odd=0


        current=0
        res=0

        for n in arr:

            current+=n

            if current%2==0:

                even+=1
                res+=odd

            else:

                odd+=1

                res+=even+1

        return res % (10**9 + 7)

                