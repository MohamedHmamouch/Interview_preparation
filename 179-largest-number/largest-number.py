class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        if sum(nums)==0:
            return "0"

        ans=[]


        for i in range(len(nums)):

            nums[i]=str(nums[i])

        def helper(s1,s2):

            left=s1+s2
            right=s2+s1

            if int(left)>int(right):

                return -1

            else: 
                return 1


        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                if helper(nums[i],nums[j])==1:

                    nums[i],nums[j]=nums[j],nums[i]

        return "".join(nums)