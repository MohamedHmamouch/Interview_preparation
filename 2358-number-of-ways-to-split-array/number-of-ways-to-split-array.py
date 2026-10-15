class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        

        total=sum(nums)

        current=0
        # n=len(nums)
        ans=[]

        for i,n in enumerate(nums):

            current+=n

            right=total-current

            if current>=right:

                if    0<=i<len(nums)-1:

                    ans.append(i)

        return len(ans)