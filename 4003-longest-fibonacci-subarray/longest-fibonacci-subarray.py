class Solution:
    def longestSubarray(self, nums: List[int]) -> int:


        if len(nums)==1:

            return 1
    
        if len(nums)==2 and nums[0]==nums[1]:
    
            return 2
    
        total=0
    
        left=0
        right=1
        max_subarray=0
        current_subbaray=0
    
        while right<len(nums)-1:
    
    
            # if nums[left]==nums[right]:
    
            #     max_subarray=max(max_subarray,right-left+1)

            current_subbaray=right-left+1
    
            if right<len(nums)-1 and nums[left]+nums[right]==nums[right+1]:
    
                start=left
    
                while right<len(nums)-1 and nums[left]+nums[right]==nums[right+1]:
    
    
                    max_subarray=max(max_subarray,(right+1)-start+1)
                    # print(start,right)
    
                    right+=1
    
                    left+=1
    
                # print(start,right)
    
            right+=1
            left+=1
    
        return max(max_subarray,current_subbaray)
        