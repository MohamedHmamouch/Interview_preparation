class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        max_profit=0

        s=prices[0]

        for i in range(1,len(prices)):

            if prices[i]-s>=0:

                max_profit+=prices[i]-s

            s=prices[i]

        return max_profit