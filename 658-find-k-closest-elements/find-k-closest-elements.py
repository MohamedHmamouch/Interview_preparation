import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap=[]

        for n in arr:

            heapq.heappush(heap,(abs(n-x),n))

        res=[]
        

        while k>0:

            val,key=heapq.heappop(heap)

            res.append(key)
            k-=1

        return sorted(res)

        


        
#         heap = []
# for cle, valeur in mon_dict.items():
#     heapq.heappush(heap, (valeur, cle))