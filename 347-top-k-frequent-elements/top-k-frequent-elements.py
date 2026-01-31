class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        import heapq

        freq={}

        for n in nums:

            freq[n]=1+freq.get(n,0)

        
        heap=[(-1*count,n) for n,count in freq.items()]
        
        heapq.heapify(heap)

        ans=[]
        while k>0:

            count,n=heapq.heappop(heap)

            ans.append(n)

            k-=1

        return ans
        