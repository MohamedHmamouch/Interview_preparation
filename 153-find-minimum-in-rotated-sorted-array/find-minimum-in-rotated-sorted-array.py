class Solution:
    def findMin(self, nums: List[int]) -> int:


        l=1
        min_element=nums[0]

        r=len(nums)-1

        while l<=r:

            mid=(l+r)//2

            if nums[mid]<=min_element:

                min_element=nums[mid]

                r=mid-1

            else:

                l=mid+1

        return min_element



        