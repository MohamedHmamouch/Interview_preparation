class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:


        res=0

        l,r=0,0
        m=0

        odd=0

        while  r<len(nums):

            odd+=1 if nums[r]%2!=0 else 0

            while l<r and odd>k:

                if nums[l]%2!=0:

                    odd-=1

                l+=1

            m=l

            if odd==k:

                while nums[m]%2==0:

                    m+=1

                res+=m-l+1

                m=l

            r+=1

        return res
                
        

