class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        

        s=set()

        ans=[]

        for i in range(len(nums)):

            if nums[i] not in s:

                s.add(nums[i])

            else:

                ans.append(nums[i])

        print(s)
        for i in range(1,len(nums)+1):

            if i not in s:

                ans.append(i)

        return ans


