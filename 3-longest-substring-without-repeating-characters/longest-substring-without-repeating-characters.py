class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:

        l=0
        r=0
        freq={}
        max_substring=0
        while r<len(nums):

            freq[nums[r]]=1+freq.get(nums[r],0)

            while l<=r and freq[nums[r]]>1:

                freq[nums[l]]-=1

                if freq[nums[l]]<0:

                    del freq[nums[l]]

                l+=1

            

            max_substring=max(r-l+1,max_substring)
            r+=1

        return max_substring