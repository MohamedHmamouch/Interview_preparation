class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        max_val=-float('inf')

        stack=[]

        for i in reversed(nums):

            if max_val>i:
            
                return True

            while stack and stack[-1]<i:

                max_val=stack.pop()

            stack.append(i)


        return False
        