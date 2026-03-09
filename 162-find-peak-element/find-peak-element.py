class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        


        l=0

        r=len(nums)-1

        while l<=r:

            mid=(l+r)//2

            prev_element=nums[mid-1] if mid-1>=0 else float('-inf')

            next_element=nums[mid+1] if mid+1<len(nums) else float('-inf')

            if prev_element<nums[mid]>next_element:

                return mid


            elif nums[mid]<next_element:

                l=mid+1

            else:

                r=mid-1
