import math
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x,n):

            if n==0:return 1

            if x==0:return 0

            half=helper(x,n//2)

            res=half*half

            return res*x if n%2!=0 else res

        return helper(x,n) if n>0 else 1/helper(x,abs(n))

        