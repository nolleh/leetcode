from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # dp[i] = maximum money can rob up to house i
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # Can't rob both house 0 and 1

        for i in range(2, n):
            # Either skip current house (dp[i-1])
            # Or rob current house (dp[i-2] + nums[i])
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
