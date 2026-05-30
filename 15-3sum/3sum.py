class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        ans=set()

        nums.sort()

        for i in range(len(nums)):


            left=i+1

            right=len(nums)-1


            while left<right:


                if left!=i and right!=i and nums[left]+nums[right]+nums[i]==0:

                    ans.add((nums[left],nums[right],nums[i]))

                    left+=1

                    right-=1

                elif nums[left]+nums[right]+nums[i]>0:

                    right-=1


                else:

                    left+=1

        return [list(triplets) for triplets in ans]