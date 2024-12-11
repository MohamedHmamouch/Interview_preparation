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

            total=sum([val for key,val in freq.items()])

            res=max(res,total)
            r+=1

        return res
        