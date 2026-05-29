class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums)==1:

            return True

        left, right=0,1

        increasing=False
        while right<len(nums):


            if nums[left]<=nums[right]:

                increasing=True

            else:

                increasing=False

                break

            left+=1

            right+=1

        if not increasing:

            left, right=0,1

        decreasing=False
        while right<len(nums):


            if nums[left]>=nums[right]:

                decreasing=True

            else:

                decreasing=False

                break

            left+=1

            right+=1

        
        return True if  increasing or  decreasing else False

