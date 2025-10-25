class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        duplicates=[]

        for n in nums:

            m=abs(n)

            if nums[m-1]<0:

                duplicates.append(m)
            else:

                nums[m-1]*=-1

        return duplicates[0]