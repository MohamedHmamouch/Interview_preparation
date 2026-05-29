class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        freq={}

        heap=[]

        for n in nums:

            freq[n]=freq.get(n,0)+1


        
        heap=[(-1*v,num) for num,v in freq.items()]

        heapq.heapify(heap)

        ans=[]
        while k>0:

            _,val=heapq.heappop(heap)

            ans.append(val)
            k-=1

        return ans




        

        # sorted_freq=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))

        # print(sorted_freq)

        # return [num for num,_ in sorted_freq.items()][:k]