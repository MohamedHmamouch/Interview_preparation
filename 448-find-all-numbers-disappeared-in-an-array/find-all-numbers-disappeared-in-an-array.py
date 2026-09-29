class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        

        single_num=set(nums)
        ans=[]

        for i in range(1,len(nums)+1):

            if i not in single_num:
                ans.append(i)

        return ans