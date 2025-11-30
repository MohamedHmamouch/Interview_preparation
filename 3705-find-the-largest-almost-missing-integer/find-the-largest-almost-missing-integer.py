class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:


        l,r=0,k-1

        from collections import defaultdict

        freq=defaultdict(list)


        while r<len(nums):


            for i in set(nums[l:r+1]):
                

                freq[i].append(nums[l:r+1])

            
            r+=1
            l+=1

        print(freq)

        
        candidates=sorted([k for k,v in freq.items() if len(v)==1],reverse=True)

        print(candidates)

        return candidates[0] if len(candidates) else -1