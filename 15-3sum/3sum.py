class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:


        nums.sort()
        s=set()

        for i in range(len(nums)):

            total=nums[i]

            start=i

            left=i+1

            right=len(nums)-1        

            while left<right:

                if total+nums[left]+nums[right]==0 and left!=i and right!=i:

                    s.add((nums[i],nums[left],nums[right]))

                    left+=1

                    right-=1

                elif total+nums[left]+nums[right]>0:

                    right-=1


                else:

                    left+=1


        return list(s)