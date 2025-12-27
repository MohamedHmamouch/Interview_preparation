class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        

        num_pairs=0

        r=len(nums)-1
        l=0
        nums.sort()

        while l<r:

            if nums[l]+nums[r]==k:

                l+=1
                r-=1
                num_pairs+=1

            elif nums[l]+nums[r]>k:

                r-=1

            else:

                l+=1

        return num_pairs

