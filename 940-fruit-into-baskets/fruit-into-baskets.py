class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        

        freq={}
        unique_fruits=set(fruits)

        l,r=0,0

        total=0

        while r<len(fruits):

            freq[fruits[r]]=1+freq.get(fruits[r],0)


            while l<r and len(freq)>2:

                freq[fruits[l]]-=1

                if freq[fruits[l]]<=0:

                    del freq[fruits[l]]

                l+=1

            total=max(total,r-l+1)
            r+=1

        return total