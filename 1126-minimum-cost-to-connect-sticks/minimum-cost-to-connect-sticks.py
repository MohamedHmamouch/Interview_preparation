class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        

        ans=0


        import heapq

        heapq.heapify(sticks)


        while len(sticks)>1:

            val1,val2=heapq.heappop(sticks),heapq.heappop(sticks)

            print(f"before {val1} and {val2} previous answer{ans}")

            temp=val1+val2

            ans+=val1+val2

            print(f"before {val1} and {val2} new answer {ans}")

            heapq.heappush(sticks,temp)

        return ans
