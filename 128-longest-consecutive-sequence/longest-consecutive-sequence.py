class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_nums=set(nums)
        

        max_consecutive=0

        for n in set_nums:

            current_consecutive=0

            if n-1 in set_nums:

                continue

            else:

                start=n

                length=0

                while n+length in set_nums:

                    length+=1

                    current_consecutive+=1

            max_consecutive=max(max_consecutive,current_consecutive)

        return max_consecutive