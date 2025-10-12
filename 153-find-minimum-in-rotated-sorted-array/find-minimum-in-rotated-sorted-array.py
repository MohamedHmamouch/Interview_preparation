class Solution:
    def findMin(self, nums: List[int]) -> int:


        left=0
        right=len(nums)-1

        min_element=nums[0]

        while left<=right:

            mid=(left+right)//2
            # print(mid)

            if nums[mid]>=min_element:

                left=mid+1


            elif nums[mid]<=min_element:

                min_element=min(nums[mid],min_element)

                right=mid-1

        return min_element
        