class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        freq={}

        for n in nums:

            freq[n]=1+freq.get(n,0)


        
        sorted_freq=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))

        sorted_list=[key for key in sorted_freq.keys()]
        print(sorted_list)

        return sorted_list[:k]