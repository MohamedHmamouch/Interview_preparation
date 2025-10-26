class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        l,r=0,0

        max_picked=0

        basket={}
        total=0

        while r<len(fruits):

            basket[fruits[r]]=1+basket.get(fruits[r],0)
            total+=1

            while l<=r and len(basket)>2:

                total-=1
                basket[fruits[l]]-=1

                if basket[fruits[l]]<=0:

                    del basket[fruits[l]]

                l+=1

            r+=1
            max_picked=max(max_picked,total)

        return max_picked


