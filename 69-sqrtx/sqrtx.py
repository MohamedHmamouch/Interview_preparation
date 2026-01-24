
import math
class Solution:
    def mySqrt(self, x: int) -> int:


        l=1
        r=x

        nearest=x

        while l<=r:

            mid=(l+r)//2

            if mid*mid==x:

                return mid

            elif mid*mid>x:

                r=mid-1

            else:

                nearest=mid
                l=mid+1

        return nearest

        