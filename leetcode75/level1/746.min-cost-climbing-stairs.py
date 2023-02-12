class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # start idx 0 or 1
        # if you pay, then you can 1 or 2 step
        # return minimum cost
        memo = [0] * len(cost)

        # idx's minimum cost
        def minimum(n: int) -> int:
            if memo[n] != 0:
                return memo[n]
            if n >= len(cost) - 2:
                return cost[n]
            cost_val = cost[n] + min(minimum(n + 2), minimum(n + 1))
            memo[n] = cost_val
            return cost_val

        return min(minimum(0), minimum(1))
