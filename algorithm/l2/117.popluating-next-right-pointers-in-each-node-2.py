from collections import deque


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root
        q = deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                n = q.popleft()
                if prev:
                    prev.next = n
                prev = n
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return root
