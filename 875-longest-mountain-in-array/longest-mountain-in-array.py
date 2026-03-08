class Solution:
    def longestMountain(self, nums: List[int]) -> int:

        ans=0

        for i in range(len(nums)):

            left=i-1
            right=i+1


            if left>=0 and right<len(nums) and nums[left]<nums[i]>nums[right]:

                while left-1>=0 and nums[left]>nums[left-1]:

                    left-=1


                while right+1<len(nums) and nums[right]>nums[right+1]:

                    right+=1

                ans=max(ans,right-left+1)

            
        return ans