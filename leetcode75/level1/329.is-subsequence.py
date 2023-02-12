class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0:
            return True

        for tc in t:
            if len(s) > i and tc == s[i]:
                i += 1

        if i < len(s):
            return False
        return True
