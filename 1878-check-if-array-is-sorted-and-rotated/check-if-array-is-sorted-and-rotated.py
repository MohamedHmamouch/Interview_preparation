class Solution:
    def check(self, nums: List[int]) -> bool:
        

        num_rotation=0
        sorted_nums=sorted(nums)

        while num_rotation<=len(nums):

            current_list=[0]*len(nums)

            for i in range(len(nums)):

                current_list[(i+num_rotation)%len(nums)]=nums[i]

            
            if current_list==sorted_nums:

                return True
            
            num_rotation+=1

        return False