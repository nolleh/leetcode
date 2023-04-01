class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add when we know it will remain a valid sequence.
        # keeping track of the number of opening and closing brackets we have placed so far

        ans = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()

        backtrack()
        return ans
