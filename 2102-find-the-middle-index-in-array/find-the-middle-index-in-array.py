class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        if len(nums)==1:

            return 0

        n=len(nums)

        forward_pass=[0]*(n)
        forward_pass[0]=nums[0]


        for k in range(1,len(nums)):


            forward_pass[k]=nums[k]+forward_pass[k-1]


        backward_pass=[0]*(n)
        backward_pass[n-1]=nums[n-1]


        for j in range(len(nums)-2,-1,-1):

            backward_pass[j]=nums[j]+backward_pass[j+1]


        print(forward_pass)

        print(backward_pass)

        for i in range(len(nums)):


            if backward_pass[i]==forward_pass[i]:

                return i

        return -1