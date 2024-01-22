class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split("/")
        for d in dirs:
            if d == "":
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            elif d != ".":
                stack.append(d)

        return "/" + "/".join(stack)
