class Solution:
    def totalFruit(self, nums: List[int]) -> int:

        n=len(nums)
        freq={}
        l,r=0,0
        res=0

        while r<n:

            freq[nums[r]]=1+freq.get(nums[r],0)

            while len(freq)>2 and l<=r:

                freq[nums[l]]-=1

                if freq[nums[l]]==0:

                    del freq[nums[l]]

                l+=1


            res=max(res,r-l+1)
            r+=1

        return res
        