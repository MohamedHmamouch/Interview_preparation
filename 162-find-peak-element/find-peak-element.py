class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums)==1:

            return 0

        elif len(nums)==2:

            if nums[0]>=nums[1]:

                return 0

            else:

                return 1

        elif nums[len(nums)-1]>nums[len(nums)-2]:

            return len(nums)-1

        else:

            l=0
            r=len(nums)-1

            while l<=r:

                mid=(l+r)//2

                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:

                    return mid

                elif nums[mid]<nums[mid+1]:

                    l=mid+1

                else:
                    r=mid-1

                