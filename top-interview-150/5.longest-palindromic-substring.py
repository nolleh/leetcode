class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand the palindrome from the center
        def expands(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # last expands is not palindrome, so return the previous index
            return left + 1, right - 1

        minimum_l = 0
        maximum_r = 0

        for center in range(len(s)):
            minl, maxr = expands(center, center)
            minl2, maxr2 = expands(center, center + 1)

            if maxr - minl > maximum_r - minimum_l:
                minimum_l = minl
                maximum_r = maxr

            if maxr2 - minl2 > maximum_r - minimum_l:
                minimum_l = minl2
                maximum_r = maxr2

        return s[minimum_l : maximum_r + 1]

    def longestPalindromeDP(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # dp[i][j] = s[i:j+1] is palindrome or not
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        # base case: single character
        for i in range(n):
            dp[i][i] = True

        # fill the table
        # length: 2, 3, 4, ... n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # ending index

                if length == 2:
                    # base case: two characters
                    dp[i][j] = s[i] == s[j]
                else:
                    # recurrence: dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                # update max length palindrome
                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length

        return s[start : start + max_len]
