class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        unique_element=len(set(nums))

        freq={}

        l,r=0,0

        count=0

        while r<len(nums):

            freq[nums[r]]=1+freq.get(nums[r],0)

            while l<=r and len(freq)>=unique_element:

                freq[nums[l]]-=1

                if freq[nums[l]]<=0:

                    del freq[nums[l]]

                l+=1

            r+=1


            count+=l

        return count