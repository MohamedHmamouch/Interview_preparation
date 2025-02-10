class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        counter=0
        l,r=0,len(nums)-1

        while l<r:

            mid=(l+r)//2

            if nums[l]+nums[r]==k:

                counter+=1
                l+=1
                r-=1

            elif nums[l]+nums[r]>k:

                r-=1

            elif nums[l]+nums[r]<k:

                l+=1

        return counter
        