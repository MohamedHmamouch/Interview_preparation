class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:


        l,r=0,0
        freq={}
        total=0
        res=0
        n=len(nums)

        while r<n:

            total+=nums[r]
            freq[nums[r]]=1+freq.get(nums[r],0)

            while freq[nums[r]]>1 or r-l+1>k:

                total-=nums[l]
                freq[nums[l]]-=1

                if freq[nums[l]]<=0:

                    del freq[nums[l]]

                l+=1

            if r-l+1==k:

                res=max(total,res)

            r+=1
        return res
        