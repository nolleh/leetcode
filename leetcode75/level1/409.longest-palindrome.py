class Solution:
    def longestPalindrome(self, s: str) -> int:
        # build longest palindrome.
        # 1. count same - letters
        # 2. you can put only 1 letter for longer palindrome
       
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
