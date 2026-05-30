class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq

        heap=[-1*num for num in nums]

        heapq.heapify(heap)

        print(heap)

        counter=1

        while k>0:

            val=heapq.heappop(heap)

            k-=1

        return -1*val

