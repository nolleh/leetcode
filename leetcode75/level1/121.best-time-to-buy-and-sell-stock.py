class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximize profit by choosing a single day to buy one stock, and choosing different day in the future to sell the stock.
        # reutrn maximum profit. cannot achieve any profit, return 0.

        if len(prices) == 0:
            return 0
        if len(prices) == 1:
            return 0

        maximum = 0
        minimum = prices[0]
        for p in prices:
            maximum = max(maximum, p - minimum)
            minimum = min(minimum, p)
        return maximum
