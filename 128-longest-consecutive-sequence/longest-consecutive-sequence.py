class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        seen=set(nums)

        max_length=0

        for k in seen:

            
            if k-1 in seen:

                continue
            else:

                start=k

            length=1

            while start+length in seen:

                length+=1

            
            max_length=max(max_length,length)

        return max_length
        