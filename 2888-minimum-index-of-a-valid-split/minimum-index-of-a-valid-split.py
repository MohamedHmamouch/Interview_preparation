class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        best_index=-1

        from collections import Counter

        mapper=Counter(nums)
        
        x=sorted(mapper.items(),key=lambda item:item[1],reverse=True)[0][0]
        print(x)

        left_count=0

        for i,n in enumerate(nums):

            left_count+=1 if n==x else 0

            right_count=mapper[x]-left_count


            if left_count>(i+1)//2 and right_count>(len(nums)-i-1)//2:

                return i 

        return -1