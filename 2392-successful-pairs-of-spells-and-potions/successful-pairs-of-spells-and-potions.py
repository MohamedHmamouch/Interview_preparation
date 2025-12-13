class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()

        ans=[]

        for spell in spells:

            count=0

            l,r=0,len(potions)-1


            while l<=r:

                mid=(l+r)//2

                if spell*potions[mid]>=success:

                    count+=r-mid+1

                    r=mid-1


                else:

                    l=mid+1


            ans.append(count)

        return ans
        