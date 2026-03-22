class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        

        l=0

        is_odd=True if nums[l]%2!=0 else False

        for r in range(len(nums)):

            
            if nums[r]%2==0 and nums[l]%2!=0:

                nums[l],nums[r]=nums[r],nums[l]
                l+=1

            if nums[l]%2==0:
                l+=1
            # else:

            #     l=r

        return nums