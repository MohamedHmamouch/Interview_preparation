class Solution:
    def characterReplacement(self, nums: str, k: int) -> int:

        l=0
        r=0
        m=0
        max_substring=0
        freq={}
        while r<len(nums):


            freq[nums[r]]=1+freq.get(nums[r],0)

            m=max(freq[nums[r]],m)

            while l<=r and r-l+1-m>k:

                freq[nums[l]]-=1
                m=max(m,freq[nums[l]])

                if freq[nums[l]]<=0:

                    del freq[nums[l]]

                l+=1

            max_substring=max(r-l+1,max_substring)
            r+=1


        return max_substring