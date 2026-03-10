class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:

        l,r=0,len(nums)-1

        while r-l+1>k:

            if abs(nums[r]-x)<abs(nums[l]-x):

                l+=1


            elif abs(nums[l]-x)<abs(nums[r]-x):

                r-=1


            else:

                r-=1

        return nums[l:r+1]
        