class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        freq={}

        for n in nums:

            freq[n]=1+freq.get(n,0)

        heap=[]

        heap=[(-1*val,key) for key,val in freq.items()]

        import heapq

        heapq.heapify(heap)

        ans=[]
        while k>0:

            val,key=heapq.heappop(heap)

            ans.append(key)
            k-=1

        return ans