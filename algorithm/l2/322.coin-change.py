class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins: representing coins of different denomianations
        # amount: total amount of money
        # the fewest number of coins that need to make up that amount.

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                # dp[x] until now, F(x) minimum coin change.
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
