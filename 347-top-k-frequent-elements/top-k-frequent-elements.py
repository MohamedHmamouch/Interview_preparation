class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        
        freq={}
        for n in nums:

            freq[n]=1+freq.get(n,0)


        sorted_list=[key for key in dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))]

        print(sorted_list)

        return sorted_list[:k]