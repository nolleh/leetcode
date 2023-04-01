class Solution:
    def numDecodings(self, s: str) -> int:
        sint = [int(char) for char in s]
        if sint[0] == 0:
            return 0
        dp = [1, 1]

        for i in range(1, len(s)):
            pre, curr = sint[i - 1], sint[i]
            if pre != 0 and 10 <= pre * 10 + curr <= 26:
                if curr == 0:
                    dp.append(dp[i - 1])
                else:
                    dp.append(dp[i] + dp[i - 1])
            else:
                if curr == 0:
                    dp.append(0)
                    break
                dp.append(dp[i])

        return dp[-1]
