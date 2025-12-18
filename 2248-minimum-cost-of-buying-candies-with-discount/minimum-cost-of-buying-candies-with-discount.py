class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        total=0

        count=0


        cost.sort()

        for i in range(len(cost)-1,-1,-1):


            if count<2:

                total+=cost[i]
                count+=1

            elif count==2:

                count=0

        return total