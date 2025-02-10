class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        minleft=[0]*len(nums)
        maxright=[0]*len(nums)

        minleft[0]=nums[0]
        maxright[-1]=nums[-1]

        for i in range(1,len(nums)-1):

            minleft[i]=min(nums[i],minleft[i-1])

        for i in range(len(nums)-2,-1,-1):

            maxright[i]=max(nums[i],maxright[i+1])

        print(minleft)
        print(maxright)

        for i in range(1,len(nums)-1):


            if minleft[i-1]<nums[i]<maxright[i+1]:

                return True
        return False


        