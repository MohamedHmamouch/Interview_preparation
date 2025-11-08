class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums)==1:

            return 0
        

        l,r=0,len(nums)-1

        while l<=r:

            mid=(l+r)//2

            val_1=nums[mid+1] if mid+1<len(nums) else -1*float('inf')
            val_2=nums[mid-1] if mid-1>=0 else -1*float('inf')

            if nums[mid]>val_2 and nums[mid]>val_1:

                return mid

            elif nums[mid]>val_2:

                l=mid+1

            else:

                r=mid-1

