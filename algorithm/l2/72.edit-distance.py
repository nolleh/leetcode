# HARD
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        if l1 == 0:
            return l2
        if l2 == 0:
            return l1
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for w1i in range(1, l1 + 1):
            dp[w1i][0] = w1i
        for w2i in range(1, l2 + 1):
            dp[0][w2i] = w2i

        for w1i in range(1, l1 + 1):
            for w2i in range(1, l2 + 1):
                if word2[w2i - 1] == word1[w1i - 1]:
                    dp[w1i][w2i] = dp[w1i - 1][w2i - 1]
                else:
                    dp[w1i][w2i] = (
                        min(
                            dp[w1i - 1][w2i],
                            min(dp[w1i][w2i - 1], dp[w1i - 1][w2i - 1]),
                        )
                        + 1
                    )

        return dp[-1][-1]
