class Solution:
    def mySqrt(self, x: int) -> int:
        

        closest=0

        l,r=0,x


        while l<=r:


            mid=(l+r)//2


            if mid**2==x:

                return mid


            elif mid**2>x:

                r=mid-1

            else:

                closest=max(closest,mid)

                l=mid+1

        return closest