class Solution:
    def minimumCost(self, cost: List[int]) -> int:



        total_cost=0
        
        num_candies=0

        cost.sort(reverse=True)

        for r in cost:

            total_cost+=r
            num_candies+=1

            if num_candies>2:

                num_candies=0
                total_cost-=r

        return total_cost
        