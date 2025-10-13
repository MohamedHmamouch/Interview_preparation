class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        import math


        left=1
        right=max(piles)
        min_speed=right

        def piles_finished(h,k):

            total_hours=0

            for p in piles:

                total_hours+=math.ceil(p/k)

            return total_hours<=h



        while left<=right:

            mid=(left+right)//2

            if piles_finished(h=h,k=mid):

                min_speed=min(mid,min_speed)
                right=mid-1

            else:

                left=mid+1
  


        return min_speed


        