from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        ## dp[i] = True if s[0:i] can be segmented into words in wordDict
        for i in range(1, n + 1):
            for word in wordDict:
                ## if the last word is in the wordDict, and the previous part is also segmented,
                # then the current part is also segmented
                if i >= len(word) and s[i - len(word) : i] == word:
                    dp[i] = dp[i] or dp[i - len(word)]
        return dp[n]
