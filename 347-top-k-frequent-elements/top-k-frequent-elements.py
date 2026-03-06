class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq={}

        for i in nums:

            freq[i]=1+freq.get(i,0)

        

        freq_sorted=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))

        print(freq_sorted)


        return [keys for keys,v in freq_sorted.items()][:k]