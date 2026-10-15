class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:

        change=False

        for i in range(1,len(nums)):


            if nums[i-1]>nums[i]:

                if change:

                    return False

                else:

                    change=True

                    if i-2>=0 and nums[i]<nums[i-2]:

                        nums[i]=nums[i-1]

                    else:
                        nums[i-1]=nums[i]

        return True