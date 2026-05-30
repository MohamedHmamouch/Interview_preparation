class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap=[]

        ans=[]

        for x,y in points:

            distance=((x**2)+y**2)**0.5

            heap.append((distance,x,y))


        heapq.heapify(heap)
        while k>0:

            distance,x,y=heapq.heappop(heap)

            ans.append((x,y))

            k-=1

        return ans