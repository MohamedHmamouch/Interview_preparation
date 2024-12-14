class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        total=0
        res=0
        l,r=0,0
        freq={}

        n=len(nums)
        maxfreq=0

        while r<n:

            total+=nums[r]
            freq[nums[r]]=1+freq.get(nums[r],0)
            
            while freq[nums[r]]>1:

                total-=nums[l]
                freq[nums[l]]-=1

                if freq[nums[l]]<=0:

                    del freq[nums[l]]

                l+=1

            res=max(res,total)
            r+=1

        return res
        