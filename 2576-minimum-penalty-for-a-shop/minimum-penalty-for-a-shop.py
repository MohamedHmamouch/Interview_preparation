class Solution:
    def bestClosingTime(self, customers: str) -> int:

        profit = 0
        max_profit = 0
        best_index = 0

        for i, char in enumerate(customers):

            if char == 'Y':
                profit += 1
            else:
                profit -= 1

            if profit > max_profit:
                max_profit = profit
                best_index = i + 1

        return best_index