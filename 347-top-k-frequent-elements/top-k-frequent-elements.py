class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        maxfreq=[]

        freq={}

        for i,n in enumerate(nums):

            freq[n]=1+freq.get(n,0)

        
        freq={k:freq[k] for k in sorted(freq,key=lambda k:freq[k],reverse=True)}


        for kx,v in freq.items():

            maxfreq.append(kx)


        return maxfreq[:k]