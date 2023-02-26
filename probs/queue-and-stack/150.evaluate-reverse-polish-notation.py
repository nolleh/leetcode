class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        op = set(["+", "-", "*", "/"])
        for t in tokens:
            if t in op:
                o2 = int(s.pop())
                o1 = int(s.pop())
                r = 0
                if t == "+":
                    r = o1 + o2
                elif t == "-":
                    r = o1 - o2
                elif t == "*":
                    r = o1 * o2
                else:
                    r = int(o1 / o2)
                s.append(r)
            else:
                s.append(t)
        return int(s[-1])
