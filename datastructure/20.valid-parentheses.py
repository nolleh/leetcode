class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # for c in s:
        #     if c == '(' or c == '[' or c == '{':
        #         stack += [c]
        #         continue
        #     if len(stack) == 0:
        #         return False
        #     if c == ')' and stack[-1] != '(':
        #         return False
        #     elif c == ']' and stack[-1] != '[':
        #         return False
        #     elif c == '}' and stack[-1] != '{':
        #         return False
        #     stack.pop()
        # return len(stack) == 0
        match = {"{": "}", "[": "]", "(": ")"}

        for c in s:
            if c in ["}", "]", ")"]:
                if not stack or match[stack[-1]] != c:
                    return False
                if stack:
                    stack.pop()
            else:
                stack += c
        return not stack
