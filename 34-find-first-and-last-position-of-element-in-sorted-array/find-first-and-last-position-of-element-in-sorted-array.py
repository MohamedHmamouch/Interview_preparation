class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        l,r=0,len(nums)-1

        while l<=r:

            mid=(l+r)//2

            if nums[mid]==target:

                start=mid

                end=mid

                while start<len(nums) and nums[start]==target:

                    start+=1

                while end>=0 and nums[end]==target:

                    end-=1



                
                return [end+1,start-1]

            elif target>nums[mid]:

                l=mid+1
            else:

                r=mid-1
        return [-1,-1]