class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        import math


        l,r=1,max(piles)


        def can_eat(mid):

            total_hours=0


            for pile in piles:


                total_hours+=math.ceil(pile/mid)

            return total_hours<=h

    

        min_speed=float('inf')

        while l<=r:

            mid=(l+r)//2

            if can_eat(mid):

                min_speed=min(mid,min_speed)

                r=mid-1
            else:

                l=mid+1

        return min_speed

            
        