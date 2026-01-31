class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        unique_element=set(nums)

        max_length=0
        for n in unique_element:

            if n-1 in unique_element:

                continue


            else:

                start=n

                length=1

                while n+length in unique_element:

                    length+=1

            max_length=max(length,max_length)

        return max_length