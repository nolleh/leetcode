class Solution:
    def integerBreak(self, n: int) -> int:
        # break it into the sum of k positive integers, where k >= 2, and maixmize the product of those integers.
        # ex. 10 = 3 + 3 + 4 => 3 * 3 * 4 = 36
        if n == 2:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2

        for i in range(4, n + 1):
            dp[i] = i
            for j in range(1, i):
                # being 1,2 or 3 max dpwer would be that number
                # unlike 5 6 7... where max dp are like 2*3,3*3,3*4...
                x = j if j <= 3 else dp[j]
                y = i - j if i - j <= 3 else dp[i - j]
                dp[i] = max(dp[i], x * y)
        return dp[n]
