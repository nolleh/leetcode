class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 'YOU CAN ONLY HOLD AT MOST ONE'

        cost = -1
        profit = 0
        prices.append(0)
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1]:
                if cost != -1 and prices[i]:
                    profit += prices[i] - cost
                    cost = -1
            elif prices[i] < prices[i + 1] and cost == -1:
                cost = prices[i]
        return profit
