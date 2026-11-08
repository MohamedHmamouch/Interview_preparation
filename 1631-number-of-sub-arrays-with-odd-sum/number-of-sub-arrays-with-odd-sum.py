class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:


        prefix=0

        odd=0

        even=0

        res=0

        mod=(10**9)+7

        for n in arr:

            prefix+=n%mod

            if prefix%2==0:

                even+=1
                res+=odd

            else:

                odd+=1

                res+=1+even

        return res%mod
