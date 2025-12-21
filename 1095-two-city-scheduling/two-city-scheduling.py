class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        total_cost_to_a=0


        for cost_a,cost_b in costs:

            total_cost_to_a+=cost_a


        costs.sort(key=lambda x:x[1]-x[0])


        for i in range(len(costs)//2):

            total_cost_to_a+=costs[i][1]-costs[i][0]

        return total_cost_to_a