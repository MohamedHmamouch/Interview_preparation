class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        l=0
        r=0

        max_average=-1*float('inf')
        total=0

        while r<len(nums):

            total+=nums[r]

            while r-l+1>k:

                total-=nums[l]
                l+=1

            
            if r-l+1==k:

                max_average=max(max_average,total/k)

            r+=1
        print(total)
        return max_average


        