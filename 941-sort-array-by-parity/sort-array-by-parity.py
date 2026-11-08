class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        m=0

        ans=[0]*len(nums)

        left=0

        right=len(ans)-1

        while left<=right:

            if nums[m]%2==0:

                ans[left]=nums[m]

                left+=1
            
            else:

                ans[right]=nums[m]

                right-=1

            m+=1

        return ans