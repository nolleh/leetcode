class Solution:
    def reverseWords(self, s: str) -> str:
        # reverse string while still preserving whitespace and initial word order
        res = []
        ws = s.split(" ")

        # too verbose to implement reverse
        # (I've already solved O(N) reverse questions 1min ago), so use builtin method
        for w in ws:
            res += [w[::-1]]

        return " ".join(res)
