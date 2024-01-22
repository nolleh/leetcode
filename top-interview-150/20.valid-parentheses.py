class Solution:
    def isValid(self, ss: str) -> bool:
        stack = []
        match = {"{": "}", "[": "]", "(": ")"}
        for s in ss:
            if s in ["}", "]", ")"]:
                if not stack or match[stack[-1]] != s:
                    return False
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return not stack 

