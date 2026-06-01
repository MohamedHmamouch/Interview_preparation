class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        

        # left=0

        # right=c

        # while left<=right:

        #     val=left**2+right**2

        #     if val==c:

        #         return True

        #     elif val>c:

        #         right-=1

        #     else:

        #         left+=1

        # return False

        import math
        left=0

        right=int(math.sqrt(c))


        while left<=right:

            val=left**2+right**2

            if val==c:

                return True

            elif val>c:

                right-=1

            else:

                left+=1

        return False