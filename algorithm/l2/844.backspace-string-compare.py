class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def typedStr(s: str) -> str:
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack

        return typedStr(s) == typedStr(t)
